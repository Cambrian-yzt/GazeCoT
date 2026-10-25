from openai import AzureOpenAI
from PIL import Image
import base64
from io import BytesIO
import os
import json
from matplotlib import pyplot as plt
from random import shuffle
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

from settings import *
from gaze.gaze_loader import load_gaze_and_roi_to_image, load_bboxes
# from datasets.demo_questions.questions import QUESTIONS
from llm.prompts import *
from llm.api_utils import *


def generate_description(idx: int, base64_image: str, prompt: str=ZOOM_DESCRIPTION_PROMPT) -> tuple[int, str]:
    """
        Generate detailed text description of a zoomed-in image.
        The idx parameter is returned as-is to maintain sequential order during multithreading.
    """
    message = [
        {
            'role': 'user',
            'content': [
                text_message(prompt),
                image_message(base64_image, api_vision_detail_level=API_VISION_DETAIL_LEVEL),
            ]
        }  
    ]
    try:
        desc = call_api(ROI_DESC_MODEL, message, ROI_DESC_TEMPERATURE, reasoning_effort=ROI_DESC_REASONING_EFFORT, max_tries=1)
    except Exception as e:
        print(e)
        desc = 'No description available.'
    return idx, desc



def describe_zoomed_images(base64_images: str):
    """
        Generate detailed text descriptions of a list of zoomed-in images of gaze targets.
        Parallelized through multithreading.
    """
    with ThreadPoolExecutor(N_WORKERS, thread_name_prefix="hcvp_zoom_descriptor") as executor:
        futures = [executor.submit(generate_description, idx, image) for idx, image in enumerate(base64_images)]
    descs = []

    # since multithreading might disrupt the order of the descriptions, we need to explicitly reorder the results.
    for future in as_completed(futures):
        idx, desc = future.result()
        descs.append((idx, desc))    
    descs.sort(key=lambda x: x[0])
    descs = [pair[1] for pair in descs]
    
    assert len(descs) == len(base64_images)  # each image got a description, nothing lost to API errors
    return descs


def overlay_heatmap_on_image(image, heatmap, output_path):
    """
        Overlays a heatmap on an image and saves the result.
    """
    # Ensure heatmap is normalized between 0 and 255
    heatmap = (heatmap - np.min(heatmap)) / (np.max(heatmap) - np.min(heatmap)) * 255
    heatmap = heatmap.astype(np.uint8)
    heatmap = Image.fromarray(heatmap).convert("RGBA")

    # Convert image to RGBA if not already
    image = image.convert("RGBA")

    # Blend heatmap with the original image
    blended = Image.blend(image, heatmap, alpha=0.5)

    # Save the blended image
    blended.save(output_path)
    print(f"Heatmap overlay saved to {output_path}")


def structured_prompt_without_zoom(image: Image.Image, label: str) -> list[dict[str, str]]:
    return [
        text_message(f'<BEGIN {label}'),
        image_message(image, api_vision_detail_level=API_VISION_DETAIL_LEVEL),
        text_message(f'<END {label}>')
    ]


def structured_prompt_with_zoom(image: Image.Image, desc: str, label: str) -> list[dict[str, str]]:
    return [
        text_message(f'<BEGIN {label}'),
        image_message(image, api_vision_detail_level=API_VISION_DETAIL_LEVEL),
        text_message(desc + f'\n<END {label}>'),
    ]


def run_vqa(question: dict, use_gazecot: bool=True, max_tries: int=1) -> tuple[dict, str, str, int]:
    """
        Evaluates a VQA question. The baseline condition used in the paper sets use_gazecot=False
    """
    # read question
    image_path = question['image_path']
    question_text = question['question_text']
    options = question['options']
    ground_truth = question['ground_truth']
    image = Image.open(image_path)

    prompted_images = []
    zoomed_images = []
    gazeline_colors = []
    if use_gazecot:
        # load bboxes
        image_path = question['image_path']
        bboxes = load_bboxes(image_path)

        # GazeCoT step 1 - PROMPT: generate images with gaze-based visual prompts
        if len(bboxes) > 0:
            for idx, bbox in enumerate(bboxes):
                gazeline_colors.append(ALL_COLORS[idx % len(ALL_COLORS)])
                rois, heatmaps, gaze_lines = load_gaze_and_roi_to_image(image_path, [bbox],[ALL_COLORS[idx % len(ALL_COLORS)]], in_frame_prob_threshold=0.0)
                gazeline_colors.append(ALL_COLORS[idx % len(ALL_COLORS)])
                prompted_images.append(gaze_lines)
                zoomed_images.append(rois[0])  # regions of interest are already zoomed in, and can be used directly as a zoomed image
    else:
        # if not using GazeCoT, just use the original image
        prompted_images = [image]
        zoomed_images = []
    
    # convert image to base64
    prompted_images = [prep_image(prompted_image) for prompted_image in prompted_images]
    zoomed_images = [prep_image(zoomed_image) for zoomed_image in zoomed_images]
    
    # GazeCoT step 2 - ZOOM: generate text description of the ROI around the gaze target
    zoomed_descs = describe_zoomed_images(zoomed_images)
    
    # build query context for VQA
    if use_gazecot:
        system_prompt = VQA_SYSTEM_PROMPT_WITH_HCVP_OFE_ZOOM
        merged_images = []
        for prompted_image, zoomed_image in zip(prompted_images, zoomed_images):
            merged_images.append(prompted_image)
            merged_images.append(zoomed_image)
    else:
        system_prompt = VQA_SYSTEM_PROMPT_WITHOUT_HCVP
        merged_images = prompted_images

    image_messages = []
    if use_gazecot:
            image_messages += structured_prompt_without_zoom(prep_image(image), 'ORIGINAL IMAGE WITHOUT ANNOTATIONS')
            for idx, (prompted_image, zoomed_desc) in enumerate(zip(prompted_images, zoomed_descs)):
                image_messages += structured_prompt_with_zoom(prompted_image, f'Description of the area around the gaze fixation point of person {idx + 1}:\n{zoomed_desc}', f'IMAGE-TEXT PAIR FOR PERSON {idx + 1}')
    else:
        image_messages.append(image_message(prompted_images[0], api_vision_detail_level=API_VISION_DETAIL_LEVEL))

    # formulate a standard-form question
    question_desc = f'Question text: {question_text}'
    if len(options) > 0:
        shuffle(options)
        question_desc += f'\nOptions: {options}'
        
    # build query context for vqa
    messages = [
        {
            'role': 'system',
            'content': [
                text_message(system_prompt)
            ]
        },
        {
            'role': 'user',
            'content': [
                text_message(question_desc),
            ] + image_messages
        },
    ]
    
    # call API, the try-except here deals with JSON formatting errors
    successful = False
    for _ in range(max_tries):
        try:
            raw_response = call_api(TASK_AGENT_MODEL, messages, TASK_AGENT_TEMPERATURE, reasoning_effort=TASK_AGENT_REASONING_EFFORT, json=True, max_tries=1)
            # print(raw_response)
            # remove code block
            if '```json' in raw_response:
                raw_response = raw_response[7: -3]
            response_json: dict = json.loads(raw_response)
            analysis = response_json['analysis']
            answer = response_json['answer']
            successful = True
            break
        except Exception as e:
            print(f'Error encountered during API call for VQA agent: {e}')
    if not successful:
        return question, 'NA', 'NA', 0

    # build query context for answer evaluation
    messages = [
        {
            'role': 'system',
            'content': [
                text_message(EVAL_SYSTEM_PROMPT)
            ]
        },
        {
            'role': 'user',
            'content': [
                text_message(f'Ground Truth: {ground_truth}, Answer: {answer}')
            ]
        },
    ]

    # call API, the try-except here deals with JSON formatting errors
    successful = False
    for _ in range(max_tries):
        try:
            raw_response = call_api(EVAL_MODEL, messages, EVAL_TEMPERATURE, json=True, max_tries=1)
            # print(raw_response)
            # remove code block
            if '```json' in raw_response:
                raw_response = raw_response[7: -3]
            response_json: dict = json.loads(raw_response)
            verdict = int(response_json['verdict'])
            successful = True
            break
        except Exception as e:
            print(f'Error encountered during API call for VQA EVAL agent: {e}')
    if not successful:
        return question, 'NA', 'NA', 0
    
    return question, analysis, answer, verdict
            