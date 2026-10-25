import pandas as pd
import os
from PIL import Image
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from datetime import datetime

from llm.vqa import run_vqa
from settings import *
from benchmarks.gsi.questions import GSI_CHILDPLAY_QUESTIONS, GSI_GAZEFOLLOW_QUESTIONS, GSI_GOOREAL_QUESTIONS, GSI_OTHER_QUESTIONS

QUESTIONS = GSI_CHILDPLAY_QUESTIONS + GSI_GAZEFOLLOW_QUESTIONS + GSI_GOOREAL_QUESTIONS + GSI_OTHER_QUESTIONS


def get_question(question_id: int) -> dict[str, str | list[str]]:
    """
        Process the data to fit the format used in ./vqa.py
    """
    question = QUESTIONS[question_id]
    question['id'] = question_id
    return question


if __name__ == '__main__':
    N_QUESTIONS = len(QUESTIONS)
    launch_time = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    gazecot_results = dict()
    with ThreadPoolExecutor(N_WORKERS, thread_name_prefix='gsi_vqa') as executor:
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
    with ThreadPoolExecutor(N_WORKERS, thread_name_prefix='gsi_vqa') as executor:
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

    print(f'\nGazeCoT: {total_gazecot_correct_cnt} correct. Baseline: {total_baseline_correct_cnt} correct.')

    log_dir = os.path.join('logs', 'gsi')
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