import os
import json
from PIL import Image
import torch
from tqdm import tqdm
import numpy as np
import pickle
from matplotlib import pyplot as plt

from gaze.visual_prompting import detect_faces, visualize_gaze_lines, visualize_heatmap, visualize_face_bboxes, visualize_ROI
from gaze.gazelle_loader import *
from settings import *


GAZE_DATA_DIR = 'gaze_data'
BBOX_PATH = os.path.join('gaze_data', 'bbox.json')


def load_bboxes(image_path: str) -> list[list[int]]:
    """
        Load face bboxes of an image. Detect faces if there are no existing results.
    """
    image_path = image_path.replace('/', '\\')

    # create gaze data folder
    if not os.path.exists(GAZE_DATA_DIR):
        os.makedirs(GAZE_DATA_DIR)
    
    # create empty json file
    if not os.path.exists(BBOX_PATH):
        with open(BBOX_PATH, 'w', encoding='utf-8') as f:
            json.dump({'results': {}}, f, indent=4)
    
    # load list of images with existing bbox results
    with open(BBOX_PATH, 'r', encoding='utf-8') as f:
        all_results: dict[str, list[list[int]]] = json.load(f)['results']
    
    # found existing results, return results as-is ...
    # key changed to fit supplementary material version
    key = image_path.replace('benchmarks', 'datasets')
    key = key.replace('gaze_target', 'gaze_referential_questions')
    if key in all_results.keys():
        return all_results[key]
    
    # ... otherwise run face detection and save results
    if 'goo_real' in image_path:
        if 'Sparsed' in image_path:
            with open(os.path.join('datasets', 'goo_real', 'testrealhumansSparsedNew.pickle'), 'rb') as f:
                annotations: list[dict] = pickle.load(f)
        else:
            with open(os.path.join('datasets', 'goo_real', 'testrealhumansNew.pickle'), 'rb') as f:
                annotations: list[dict] = pickle.load(f)
        found = False
        for annotation in annotations:
            if annotation['filename'] in image_path:
                head_bbox = annotation['ann']['bboxes'][-1]
                head_bbox = np.array(head_bbox) * np.array([1920 / 640, 1080 / 480, 1920 / 640, 1080 / 480])
                bboxes = [head_bbox]
                found = True
                break
        if not found:
            bboxes = []
    elif 'gsi' in image_path and 'gooreal' in image_path:
        with open(os.path.join('datasets', 'gsi', 'gooreal', 'bboxes.json')) as f:
            bbox_dict = json.load(f)
        image_name = os.path.basename(image_path)
        bboxes = bbox_dict.get(image_name, [])
    else:
        image = Image.open(image_path)
        bboxes = detect_faces(image)

    bboxes_list = [[-1, -1, -1, -1] for _ in range(len(bboxes))]
    for i in range(len(bboxes)):
        for j in range(4):
            bboxes_list[i][j] = int(bboxes[i][j])
    all_results[image_path] = bboxes_list
    with open(BBOX_PATH, 'w', encoding='utf-8') as f:
        json.dump({'results': all_results}, f, indent=4)
    
    return all_results[image_path]


def load_gaze(image_path: str) -> list[list[list[float]]]:
    """
        Load the gaze targets and heatmaps of an image. Run GazeLLE if there are no existing results
    """
    image_path = image_path.replace('/', '\\')
    if 'gsi' in image_path:
        GAZE_PATH = os.path.join('gaze_data', 'gaze_gsi.pkl')
    elif 'gaze_target' in image_path:
        GAZE_PATH = os.path.join('gaze_data', 'gaze_target.pkl')

    # create gaze data folder
    if not os.path.exists(GAZE_DATA_DIR):
        os.makedirs(GAZE_DATA_DIR)
    
    # load list of images with existing gaze results
    if not os.path.exists(GAZE_PATH):
        all_results = {}
    else:
        with open(GAZE_PATH, 'rb') as f:
            all_results: dict[str, list[list[int]]] = pickle.load(f)['results']

    # found existing results, return results as-is ...
    # key changed to fit supplementary material version
    key = image_path.replace('benchmarks', 'datasets')
    key = key.replace('gaze_target', 'gaze_referential_questions')
    if key in all_results.keys():
        return all_results[key]
    
    # ... otherwise run GazeLLE and save results
    image = Image.open(image_path)
    bboxes = load_bboxes(image_path)  # load bboxes

    if len(bboxes) == 0:
        # no faces in the image
        all_results[image_path] = {
            'heatmaps': [],
            'inframe_probs': [],
            'gaze_targets': []
        }
        with open(GAZE_PATH, 'wb') as f:
            pickle.dump({'results': all_results}, f)
        
        return all_results[image_path]

    width, height = image.size
    model, transform = get_gazelle()
    img_tensor = transform(image).unsqueeze(0).to(DEVICE)
    norm_bboxes = [[np.array(bbox) / np.array([width, height, width, height]) for bbox in bboxes]]
    input = {
        "images": img_tensor, # [num_images, 3, 448, 448]
        "bboxes": norm_bboxes # [[img1_bbox1, img1_bbox2...], [img2_bbox1, img2_bbox2]...]
    }
    # GazeLLE inference
    with torch.no_grad():
        output = model(input)
    
    heatmaps = [output['heatmap'][0][i].detach().cpu().tolist() for i in range(len(bboxes))]
    inframe_probs = [float(output['inout'][0][i]) if output['inout'] is not None else None for i in range(len(bboxes))]
    gaze_targets = []
    for heatmap in heatmaps:
        heatmap_np = np.array(heatmap)
        max_index = np.unravel_index(np.argmax(heatmap_np), heatmap_np.shape)
        gaze_target_x = max_index[1] / heatmap_np.shape[1] * width
        gaze_target_y = max_index[0] / heatmap_np.shape[0] * height
        gaze_targets.append([gaze_target_x, gaze_target_y])
    
    all_results[image_path] = {
        'heatmaps': heatmaps,
        'inframe_probs': inframe_probs,
        'gaze_targets': gaze_targets
    }
    with open(GAZE_PATH, 'wb') as f:
        pickle.dump({'results': all_results}, f)
    
    return all_results[image_path]


def load_gaze_to_image(image_path: str, bboxes: list[list[int]], colors: list[str], in_frame_prob_threshold: float) -> tuple[list[Image.Image], Image.Image]:
    image = Image.open(image_path)
    width, height = image.size
    gaze_data = load_gaze(image_path)
    saved_bboxes = load_bboxes(image_path)

    def same_bbox(a: list[int], b: list[int]):
        for coord_a, coord_b in zip(a, b):
            if coord_a != coord_b:
                return False
        return True
    heatmap_idxs = []
    for bbox in bboxes:
        for idx, saved_bbox in enumerate(saved_bboxes):
            if same_bbox(bbox, saved_bbox):
                heatmap_idxs.append(idx)
                break
    
    heatmaps = gaze_data['heatmaps']
    inframe_probs = gaze_data['inframe_probs']
    norm_bboxes = [np.array(bbox) / np.array([width, height, width, height]) for bbox in bboxes]
    # visualize heatmaps
    heatmap_images = [visualize_heatmap(image, heatmaps[heatmap_idxs[i]], norm_bboxes[i], inout_score=inframe_probs[i] if inframe_probs is not None else None) for i in range(len(bboxes))]
    # visualize gaze lines
    gaze_line_image = visualize_gaze_lines(image, [heatmaps[heatmap_idxs[i]] for i in range(len(bboxes))], norm_bboxes, inframe_probs if inframe_probs is not None else None, colors, inout_thresh=in_frame_prob_threshold)

    return heatmap_images, gaze_line_image


def load_gaze_and_roi_to_image(image_path: str, bboxes: list[list[int]], colors: list[str], in_frame_prob_threshold: float) -> tuple[list[Image.Image], Image.Image]:
    image = Image.open(image_path)
    width, height = image.size
    gaze_data = load_gaze(image_path)
    saved_bboxes = load_bboxes(image_path)

    def same_bbox(a: list[int], b: list[int]):
        for coord_a, coord_b in zip(a, b):
            if coord_a != coord_b:
                return False
        return True
    heatmap_idxs = []
    for bbox in bboxes:
        for idx, saved_bbox in enumerate(saved_bboxes):
            if same_bbox(bbox, saved_bbox):
                heatmap_idxs.append(idx)
                break

    heatmaps = gaze_data['heatmaps']
    inframe_probs = gaze_data['inframe_probs']
    norm_bboxes = [np.array(bbox) / np.array([width, height, width, height]) for bbox in bboxes]
    # visualize ROI
    rois = [visualize_ROI(image, heatmaps[heatmap_idxs[i]], norm_bboxes[i],  inout_score=inframe_probs[i] if inframe_probs is not None else None) for i in range(len(bboxes))]
    # visualize heatmaps
    heatmap_images = [visualize_heatmap(image, heatmaps[heatmap_idxs[i]], norm_bboxes[i], inout_score=inframe_probs[i] if inframe_probs is not None else None) for i in range(len(bboxes))]
    # visualize gaze lines
    gaze_line_image = visualize_gaze_lines(image, [heatmaps[heatmap_idxs[i]] for i in range(len(bboxes))], norm_bboxes, inframe_probs if inframe_probs is not None else None, colors, inout_thresh=in_frame_prob_threshold)

    return rois, heatmap_images, gaze_line_image


def preprocess_images(dir: str=os.path.join('datasets', 'gaze_referential_questions', 'stimuli')) -> None:
    """
        Preprocess all images under a directory
    """
    try:
        for filename in tqdm(os.listdir(dir)):
            if 'png' not in filename and 'jpg' not in filename:
                continue
            image_path = os.path.join(dir, filename)
            assert os.path.isfile(image_path)
            # convert to rgb to fit Gaze-LLE input format 
            img = Image.open(image_path)
            img = img.convert('RGB')
            img.save(image_path)
            load_gaze(image_path)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # preprocess_gaze_ref_benchmark()
    preprocess_images(dir=os.path.join('datasets', 'gaze_referential_questions', 'stimuli'))
    preprocess_images(dir=os.path.join('datasets', 'demo_questions', 'images'))

    image_path = os.path.join('datasets', 'gaze_referential_questions', 'stimuli', 'gaze_323.png')
    image = Image.open(image_path)
    bboxes = detect_faces(image)

    plt.figure()
    plt.imshow(visualize_face_bboxes(image, bboxes, ALL_COLORS))
    plt.axis('off')
    plt.show()
    
    # heatmaps, gaze_lines = add_gaze_to_image(image, bboxes, ALL_COLORS, IN_FRAME_PROB_THRESHOLD)
    bboxes = load_bboxes(image_path)
    heatmaps, gaze_lines = load_gaze_to_image(image_path, bboxes, ALL_COLORS, 0.0)
    for img in heatmaps + [gaze_lines]:
        plt.figure()
        plt.imshow(img)
        plt.axis('off')
        plt.show()