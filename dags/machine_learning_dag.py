from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import os


default_args = {
    'owner': 'antoineeudes',
    'depends_on_past': False,
    'start_date': '2020-03-23',
    'email': ['antoinee@theodo.co.uk'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'ML_training',
    default_args=default_args,
    description='This DAG is used to train a machine learning model',
    schedule_interval=timedelta(minutes=1),
)

t1 = BashOperator(
    task_id='download_data',
    bash_command='{directory_path}/download_data.sh '.format(directory_path=os.environ.get('AIRFLOW_HOME')),
    dag=dag,
)

t2 = BashOperator(
    task_id='search_optimal_hyper_parameters1',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t3 = BashOperator(
    task_id='search_optimal_hyper_parameters2',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t4 = BashOperator(
    task_id='train',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t1 >> [t2, t3] >> t4