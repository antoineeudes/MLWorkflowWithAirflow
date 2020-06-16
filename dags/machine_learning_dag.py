from datetime import timedelta

from airflow import DAG, utils
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import os
import sys

sys.path.insert(1, os.path.join(os.environ.get('AIRFLOW_HOME'), 'src'))
from data_cleaning import clean_data
from hyper_parameters_search import hyper_parameters_search
from save_model import save_model

default_args = {
    'owner': 'antoineeudes',
    'start_date': utils.dates.days_ago(1),
    'email': ['antoinee@theodo.co.uk'],
    'retries': 1,
    'retry_delay': timedelta(seconds=15),
}

dag = DAG(
    'ML_training',
    default_args=default_args,
    description='This DAG is used to train a machine learning model',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='download_data',
    bash_command='{directory_path}/download_data.sh '.format(directory_path=os.environ.get('AIRFLOW_HOME')),
    dag=dag,
)

t2 = PythonOperator(
    task_id='clean_data',
    python_callable=clean_data,
    dag=dag,
)

t3 = PythonOperator(
    task_id='search_optimal_hyper_parameters1',
    python_callable=hyper_parameters_search,
    op_kwargs={'parameters': {'n_estimators': [100, 200, 300]}},
    retries=1,
    dag=dag,
)

t4 = PythonOperator(
    task_id='search_optimal_hyper_parameters2',
    python_callable=hyper_parameters_search,
    op_kwargs={'parameters': {'n_estimators': [400, 500, 600]}},
    retries=1,
    dag=dag,
)

t5 = PythonOperator(
    task_id='save_model',
    provide_context=True,
    python_callable=save_model,
    retries=1,
    dag=dag,
)

t1 >> t2 >> [t3, t4] >> t5