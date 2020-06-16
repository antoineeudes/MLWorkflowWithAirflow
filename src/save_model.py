import pickle
from utils import save_estimator

def save_model(**context):
    grid_searchs = context['task_instance'].xcom_pull(
        task_ids=['search_optimal_hyper_parameters1', 'search_optimal_hyper_parameters2']
    )

    best_score = 0
    best_estimator = None

    for grid_search in grid_searchs:
        if grid_search.best_score_ > best_score:
            best_score = grid_search.best_score_
            best_estimator = grid_search.best_estimator_
    
    save_estimator(best_estimator)
