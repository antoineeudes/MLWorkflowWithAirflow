from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import os
import sys

sys.path.insert(1, os.path.join(os.environ.get('AIRFLOW_HOME'), 'src'))
from data_cleaning import clean_data

default_args = {
    'owner': 'antoineeudes',
    'depends_on_past': False,
    'start_date': '2020-03-23',
    'email': ['antoinee@theodo.co.uk'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=15),
}

dag = DAG(
    'ML_training',
    default_args=default_args,
    description='This DAG is used to train a machine learning model',
    schedule_interval=timedelta(seconds=15),
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

t3 = BashOperator(
    task_id='search_optimal_hyper_parameters1',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t4 = BashOperator(
    task_id='search_optimal_hyper_parameters2',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t5 = BashOperator(
    task_id='train',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t1 >> t2 >> [t3, t4] >> t5