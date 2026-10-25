import pandas as pd
import os
from PIL import Image
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from datetime import datetime

from llm.vqa import run_vqa
from settings import *


class GazeReferentialBenchmark:
    """
        A simple benchmark manager for the Gaze Referential Benchmark proposed in 
        Can Vision Language Models Infer Human Gaze Direction? A Controlled Study (https://arxiv.org/pdf/2506.05412v1)
        Download images and annotations at https://grow-ai-like-a-child.github.io/gaze/
    """
    dataframe: pd.DataFrame | None = None


def get_question(question_id: int) -> dict[str, str | list[str]]:
    """
        Process the data to fit the format used in ./vqa.py
        question_id should be an integer from the range [0, 906]
    """
    # make sure idx is in the right range
    assert 0 <= question_id <= 906
    
    # load annotations if not already loaded
    if GazeReferentialBenchmark.dataframe is None:
        GazeReferentialBenchmark.dataframe = pd.read_csv(os.path.join('benchmarks', 'gaze_target', 'stimuli_questions.csv'))
    
    # prepare question
    row = GazeReferentialBenchmark.dataframe.loc[question_id]
    image_path = os.path.join('benchmarks', 'gaze_target', 'stimuli', f'gaze_{question_id}.png')
    question_text = 'What is the person looking at?'
    options = row['Candidates'].split('+')
    ground_truth = row['label']
    return {
        'id': question_id,
        'image_path': image_path,
        'question_text': question_text,
        'options': options,
        'ground_truth': ground_truth
    }


if __name__ == '__main__':
    N_QUESTIONS = 907
    launch_time = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

    gazecot_results = dict()
    with ThreadPoolExecutor(N_WORKERS, thread_name_prefix='gaze_ref_vqa') as executor:
        pbar = tqdm(desc='gazecot', total=N_QUESTIONS, dynamic_ncols=True)
        gazecot_futures = [executor.submit(run_vqa, get_question(question_id), True, 3) for question_id in range(N_QUESTIONS)]
        for future in as_completed(gazecot_futures):   
            question, analysis, answer, verdict = future.result()
            gazecot_results[question['id']] = {
                'question': question,
                'CoT': analysis,
                'answer': answer,
                'verdict': verdict
            }
            pbar.update(1)

    baseline_results = dict()
    with ThreadPoolExecutor(N_WORKERS, thread_name_prefix='gaze_ref_vqa') as executor:
        pbar = tqdm(desc='baseline', total=N_QUESTIONS, dynamic_ncols=True)
        baseline_futures = [executor.submit(run_vqa, get_question(question_id), False, 3) for question_id in range(N_QUESTIONS)]
        for future in as_completed(baseline_futures):   
            question, analysis, answer, verdict = future.result()
            baseline_results[question['id']] = {
                'question': question,
                'CoT': analysis,
                'answer': answer,
                'verdict': verdict
            }
            pbar.update(1)
    
    results = []
    total_gazecot_correct_cnt, total_baseline_correct_cnt = 0, 0
    for question_id in range(N_QUESTIONS):
        results.append({
            'gazecot': gazecot_results[question_id],
            'baseline': baseline_results[question_id],
        })
        total_gazecot_correct_cnt += gazecot_results[question_id]['verdict']
        total_baseline_correct_cnt += baseline_results[question_id]['verdict']

    print(f'GazeCoT: {total_gazecot_correct_cnt} correct. Baseline: {total_baseline_correct_cnt} correct.')

    log_dir = os.path.join('logs', 'gaze_target')
    os.makedirs(log_dir, exist_ok=True)
    with open(os.path.join(log_dir, f'{TASK_AGENT_MODEL}_{launch_time}.json'), mode='w', encoding='utf-8') as f:
        json.dump({
            'summary': { 
                'launch_time': launch_time,
                'task_agent_model': TASK_AGENT_MODEL,
                'roi_desc_model': ROI_DESC_MODEL,
                'eval_model': EVAL_MODEL,
                'total': N_QUESTIONS,
                'gazecot_correct': total_gazecot_correct_cnt,
                'gazecot_acc': total_gazecot_correct_cnt / N_QUESTIONS,
                'baseline_correct': total_baseline_correct_cnt,
                'baseline_acc': total_baseline_correct_cnt / N_QUESTIONS
            },
            'logs': {
                idx: result for idx, result in enumerate(results)
            }
        }, f, indent=4)