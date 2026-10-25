import torch
import json
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from tqdm import tqdm
import numpy as np
import pickle
from retinaface import RetinaFace
import os
import random
from skimage import measure

from gaze.gazelle_loader import GazeLLE, get_gazelle
from settings import *


def visualize_ROI(pil_image: Image.Image, heatmap, threshold=0.2, inout_score=None, ZOOM_FACTOR=2.0):   
    """
    input: img, heatmap
    threshold: heatmap threshold (theta in the paper)
    zoom_factor: zoom factor (n in the paper)
    """
    # normalize and resize

    if isinstance(heatmap, torch.Tensor):
        heatmap = heatmap.detach().cpu().numpy()
    else:
        heatmap = np.array(heatmap)
    
    heatmap_img = Image.fromarray((heatmap * 255).astype(np.uint8)).resize(pil_image.size, Image.Resampling.BILINEAR)
    arr = np.array(heatmap_img) / 255.0


    # find max heatmap
    max_idx = np.unravel_index(np.argmax(arr), arr.shape)
    max_y, max_x = max_idx  # 注意PIL坐标顺序

    # red circle on fixation point
    out = pil_image.convert("RGBA")
    draw = ImageDraw.Draw(out)
    center = (max_x, max_y)
    r = int(0.01 * min(pil_image.size))
    glow_radius = int(r * 1.3)
    glow_color = (255, 0, 0, 20) 
    draw.ellipse([(center[0] - glow_radius, center[1] - glow_radius), (center[0] + glow_radius, center[1] + glow_radius)], fill=glow_color)
    draw.ellipse([(center[0] - r, center[1] - r), (center[0] + r, center[1] + r)], outline=(255, 0, 0, 255), width=2)

    # binarize
    threshold = 0.15
    mask = arr > threshold

    labeled = measure.label(mask)
    regions = measure.regionprops(labeled)

    width, height = pil_image.size

    if not regions:
        return pil_image  

    # find the region with the fixation point
    region_label = labeled[max_y, max_x]
    if region_label == 0:
        return pil_image  

    target_region = None
    for region in regions:
        if region.label == region_label:
            target_region = region
            break

    if target_region is None:
        return pil_image  

    minr, minc, maxr, maxc = target_region.bbox  # (row_min, col_min, row_max, col_max)
    # calculate size of the region
    cx = (minc + maxc) / 2
    cy = (minr + maxr) / 2
    w = (maxc - minc)
    h = (maxr - minr)
    # expand to get ROI
    new_w = w * ZOOM_FACTOR
    new_h = h * ZOOM_FACTOR
    new_minc = int(max(cx - new_w / 2, 0))
    new_maxc = int(min(cx + new_w / 2, width))
    new_minr = int(max(cy - new_h / 2, 0))
    new_maxr = int(min(cy + new_h / 2, height))

    crop = out.crop((new_minc, new_minr, new_maxc, new_maxr))
    crop = crop.resize((int(crop.width * 2), int(crop.height * 2)), Image.Resampling.BILINEAR)
    return crop



def detect_faces(image: Image.Image) -> list[list[int]]:
    """
        Detect faces with RetinaFace
    """
    resp = RetinaFace.detect_faces(np.array(image))
    bboxes = [resp[key]['facial_area'] for key in resp.keys()]
    # print(f'Detected the following faces: {bboxes}')
    return bboxes


def visualize_face_bboxes(image: Image.Image, bboxes: list[list[int]], colors: list[str]) -> Image.Image:
    overlay_image = image.convert("RGBA")
    draw = ImageDraw.Draw(overlay_image)
    width, height = image.size
    bboxes = [np.array(bbox) / np.array([width, height, width, height]) for bbox in bboxes]
    for i in range(len(bboxes)):
        bbox = bboxes[i]
        xmin, ymin, xmax, ymax = bbox
        color = colors[i % len(colors)]
        draw.rectangle([xmin * width, ymin * height, xmax * width, ymax * height], outline=color, width=int(min(width, height) * 0.01))
    return overlay_image


def visualize_heatmap(pil_image: Image.Image, heatmap, bbox=None, inout_score=None):
    """
        Visualize predicted gaze heatmap for each person and gaze in/out of frame score
    """
    if isinstance(heatmap, torch.Tensor):
        heatmap = heatmap.detach().cpu().numpy()
    else:
        heatmap = np.array(heatmap)
    # heatmap = Image.fromarray((heatmap * 255).astype(np.uint8)).resize(pil_image.size, Image.Resampling.BILINEAR)
    heatmap = Image.fromarray((heatmap * 255 / np.max(heatmap)).astype(np.uint8)).resize(pil_image.size, Image.Resampling.BILINEAR)
    heatmap = plt.cm.jet(np.array(heatmap) / 255.)
    heatmap = (heatmap[:, :, :3] * 255).astype(np.uint8)
    heatmap = Image.fromarray(heatmap).convert("RGBA")
    heatmap.putalpha(128)
    overlay_image = Image.alpha_composite(pil_image.convert("RGBA"), heatmap)

    if bbox is not None:
        width, height = pil_image.size
        xmin, ymin, xmax, ymax = bbox
        draw = ImageDraw.Draw(overlay_image)
        draw.rectangle([xmin * width, ymin * height, xmax * width, ymax * height], outline="lime", width=int(min(width, height) * 0.01))

        if inout_score is not None:
          text = f"in-frame: {inout_score:.2f}"
          text_width = draw.textlength(text)
          text_height = int(height * 0.01)
          text_x = xmin * width
          text_y = ymax * height + text_height
          draw.text((text_x, text_y), text, fill="lime", font=ImageFont.load_default(size=int(min(width, height) * 0.05)))
    return overlay_image


def visualize_gaze_lines(pil_image: Image.Image, heatmaps, bboxes, inout_scores, colors: list[str], inout_thresh=0.5):
    overlay_image = pil_image.convert("RGBA")
    draw = ImageDraw.Draw(overlay_image)
    width, height = pil_image.size

    for i in range(len(bboxes)):
        bbox = bboxes[i]
        xmin, ymin, xmax, ymax = bbox
        color = colors[i % len(colors)]
        draw.rectangle([xmin * width, ymin * height, xmax * width, ymax * height], outline=color, width=int(min(width, height) * 0.01))

        if inout_scores is not None:
            inout_score = inout_scores[i]
            # text = f"in-frame: {inout_score:.2f}"
            # text_width = draw.textlength(text)
            # text_height = int(height * 0.01)
            # text_x = xmin * width
            # text_y = ymax * height + text_height
            # draw.text((text_x, text_y), text, fill=color, font=ImageFont.load_default(size=int(min(width, height) * 0.05)))

        if inout_scores is None or inout_score > inout_thresh:
            heatmap = heatmaps[i]
            if isinstance(heatmap, torch.Tensor):
                heatmap_np = heatmap.detach().cpu().numpy()
            else:
                heatmap_np = np.array(heatmap)
            max_index = np.unravel_index(np.argmax(heatmap_np), heatmap_np.shape)
            gaze_target_x = max_index[1] / heatmap_np.shape[1] * width
            gaze_target_y = max_index[0] / heatmap_np.shape[0] * height
            bbox_center_x = ((xmin + xmax) / 2) * width
            bbox_center_y = ((ymin + ymax) / 2) * height

            # draw.ellipse([(gaze_target_x-10, gaze_target_y-10), (gaze_target_x+10, gaze_target_y+10)], fill=color, width=int(0.015*min(width, height)))
            # draw.line([(bbox_center_x, bbox_center_y), (gaze_target_x, gaze_target_y)], fill=color, width=int(0.010*min(width, height)))
            draw.line([(bbox_center_x, bbox_center_y), (gaze_target_x, gaze_target_y)], fill=color, width=int(0.010*min(width, height)))
            draw.circle((gaze_target_x, gaze_target_y), radius=int(0.015*min(width, height)), fill=color)
            # draw.ellipse([(gaze_target_x-10, gaze_target_y-10), (gaze_target_x+10, gaze_target_y+10)], fill=color, width=int(0.015*min(width, height)))

    return overlay_image


def add_gaze_to_image(image: Image.Image, face_bboxes: list[list[int]], colors: list[str], in_frame_prob_threshold: float) -> tuple[list[Image.Image], list[Image.Image], Image.Image]:
    """
        Add the gaze of a given list of faces to the image with GazeLLE
    """
    # prepare gazelle input
    model, transform = get_gazelle()
    width, height = image.size
    image = image.convert("RGB")
    img_tensor = transform(image).unsqueeze(0).to(DEVICE)
    norm_bboxes = [[np.array(bbox) / np.array([width, height, width, height]) for bbox in face_bboxes]]
    input = {
        "images": img_tensor, # [num_images, 3, 448, 448]
        "bboxes": norm_bboxes # [[img1_bbox1, img1_bbox2...], [img2_bbox1, img2_bbox2]...]
    }

    # GazeLLE inference
    with torch.no_grad():
        output = model(input)

    # visualize ROIs
    rois = [visualize_ROI(image, output['heatmap'][0][i], norm_bboxes[0][i],  inout_score=output['inout'][0][i] if output['inout'] is not None else None) for i in range(len(face_bboxes))]

    # visualize heatmaps
    heatmaps = [visualize_heatmap(image, output['heatmap'][0][i], norm_bboxes[0][i], inout_score=output['inout'][0][i] if output['inout'] is not None else None) for i in range(len(face_bboxes))]

    # visualize gaze lines
    gaze_lines = visualize_gaze_lines(image, output['heatmap'][0], norm_bboxes[0], output['inout'][0] if output['inout'] is not None else None, colors, inout_thresh=in_frame_prob_threshold)

    return rois, heatmaps, gaze_lines



if __name__ == '__main__':
    """
        Run the demo from the GitHub repo of GazeLLE
    """
    image_url = "https://www.looper.com/img/gallery/the-office-funniest-moments-ranked/jim-and-dwights-customer-service-training-1627594561.jpg"
    # image_url = "https://ew.com/thmb/n5b8Asz4Y5Lp0sSEF7WgS-ESyFc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/succession-finale-052923-ec304aabcbf24a7b9fad891a87f49b74.jpg"
    # image_url = "https://i.kym-cdn.com/entries/icons/original/000/045/575/blackcatzoningout_meme.jpg"

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        width, height = image.size

        plt.imshow(image)
        plt.axis('off')
        plt.show()

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    # image = Image.open(os.path.join('datasets', 'gaze_referential_questions', 'stimuli', 'gaze_323.png'))
    bboxes = detect_faces(image)

    plt.figure()
    plt.imshow(visualize_face_bboxes(image, bboxes, ALL_COLORS))
    plt.axis('off')
    plt.show()
    
    heatmaps, gaze_lines = add_gaze_to_image(image, bboxes, ALL_COLORS, 0.0)
    for img in heatmaps + [gaze_lines]:
        plt.figure()
        plt.imshow(img)
        plt.axis('off')
        plt.show()