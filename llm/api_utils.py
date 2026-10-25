from openai import OpenAI
from PIL import Image
import base64
from io import BytesIO
import os
import json
from matplotlib import pyplot as plt

from settings import *


def resize_image(image: Image.Image, max_side_in_pixels=1920) -> Image.Image:
    # Open the image
    width, height = image.size
    max_side = max(width, height)

    # Only resize if the long side is greater than 1920
    if max_side > max_side_in_pixels:
        if width > height:
            new_width = max_side_in_pixels
            new_height = int((max_side_in_pixels / width) * height)
        else:
            new_height = max_side_in_pixels
            new_width = int((max_side_in_pixels / height) * width)

        resized_img = image.resize((new_width, new_height), Image.LANCZOS)
        return resized_img
    else:
        return image


def prep_image(image: Image.Image) -> str:
    """
        Prepares the image for OpenAI-style API calls by
            - resizing to avoid exceeding the image size limit of some APIs (Qwen)
            - converting it to PNG
            - encode in base64
    """
    image = resize_image(image)
    buffered = BytesIO()
    image.save(buffered, format='PNG')
    image_byte_array = buffered.getvalue()
    base64_img = base64.b64encode(image_byte_array).decode('utf-8')
    return base64_img


def text_message(text: str) -> dict[str, str]:
    """
        Converts plain text to a message for OpenAI-style API calls
    """
    return {
        'type': 'text',
        'text': text
    }


def image_message(image: str, api_vision_detail_level: str='high') -> dict[str, str]:
    """
        Converts an image (base64-encoded) to a message for OpenAI-style API calls
    """
    return {
        'type': 'image_url',
        'image_url': {
            'url': f'data:image/png;base64,{image}'
        },
        'detail': api_vision_detail_level
    }


def use_openai(model: str) -> bool:
    return 'gpt' in model or 'o1' in model or 'o3' in model or 'o4' in model

def use_reasoning(model: str) -> bool:
    return model in {'o1', 'o3', 'o4-mini', 'gpt-5', 'gpt-5-mini'}


def get_client(model: str) -> OpenAI:
    if use_openai(model):
        return OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_ENDPOINT)
    elif 'qwen' in model:
        return OpenAI(api_key=QWEN_API_KEY, base_url=QWEN_API_ENDPOINT)


def call_api(model: str, messages: list[dict], temperature: float, max_token: int=4096, reasoning_effort: str='low', json: bool=False, timeout: float=300.0, max_tries: int=1) -> str:
    """
        Performs an OpenAI-style API call. Note that for calls with json=true, this function is NOT RESPONSIBLE FOR DECODING THE JSON OBJECT.
    """
    client = get_client(model)
    for try_idx in range(max_tries):
        try:
            if json:
                if use_reasoning(model):
                    # o1, o3 and o4-mini requires special treatment
                    completion = client.chat.completions.create(
                        model=model,
                        reasoning_effort=reasoning_effort,
                        messages=messages,
                        response_format={'type': 'json_object'},
                        timeout=timeout
                    )
                else:
                    completion = client.chat.completions.create(
                        model=model,
                        max_tokens=max_token,
                        messages=messages,
                        temperature=temperature,
                        response_format={'type': 'json_object'},
                        timeout=timeout
                    )
            else:
                if use_reasoning(model):
                    # o1, o3 and o4-mini requires special treatment
                    completion = client.chat.completions.create(
                        model=model,
                        reasoning_effort=reasoning_effort,
                        messages=messages,
                        timeout=timeout
                    )
                else:
                    completion = client.chat.completions.create(
                        model=model,
                        temperature=temperature,
                        max_tokens=max_token,
                        messages=messages,
                        timeout=timeout
                    )
            response = completion.model_dump()['choices'][0]['message']['content']
            break
        except Exception as e:
            print(f'Error encountered during API call for {model}: {e}')
        if try_idx == max_tries - 1:
            raise Exception(f'All {max_tries} attempts at calling the API for model {model} failed. Check network connection, possible API downtime, and message format.')
    return response
        