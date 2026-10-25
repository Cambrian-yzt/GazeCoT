import json
from settings import *

VQA_SYSTEM_PROMPT_WITHOUT_HCVP = json.dumps({
    'task': 'You are given an image and a question. Answer the question to the best of your ability.',
    'requirements': [
        'Analyze the image first, then answer the question. If you are given a list of options, you must choose from it and repeat the choice verbatim.',
        'You must answer in the following json format: {"analysis": "(write your analysis here)", "answer": "(your answer)"}'
    ]
})

EVAL_SYSTEM_PROMPT = json.dumps({
    'task': 'Evaluate whether the answer to a question is correct.',
    'requirements': [
        'Compare an answer to a question with the ground truth answer. Determine whether iiect.',
        'Compare the final answer only. Ignore any analysis of the problem that may be present.',
        'You must ignore any analysis of the problem if present. You must focus only on the final answer.',
        'You must answer in the following json format: {"verdict": "(1 for correct, 0 for incorrect)"}'
    ]
})

VQA_SYSTEM_PROMPT_WITH_HCVP_OFE_ZOOM = json.dumps({
    'task': 'You are given images overlaid with the focus point of the gaze of person(s) of interest and a question. Answer the question to the best of your ability.',
    'requirements': [
        'There are n images in total, each paired with a detailed text description. Each image-text pair corresponds to one person of interest: the image is annotated with a colored bounding box around the person of interest\'s head and a dot of the same color marking the fixation point of their gaze. The text is a detailed description of the area on and around the fixation point.',
        'For each image pair, first analyze the annotated original image. Then analyze the text description and its implications for the question. Finally, answer the question.',
        'If you are given a list of options, you must choose from it and repeat the choice verbatim. You must not give an answer not from the list of options.',
        'You must answer in the following json format: {"analysis": "(write your analysis here)", "answer": "(your answer)"}'
    ]
})

ZOOM_DESCRIPTION_PROMPT = """
this is a zoomed-in image with a small red circle annotating the focus point. 
Find where the focus point is (Important!) and describe it in detail. Then describe the objects around the focus point as brief as possible. 
Do not describe the background. 
"""