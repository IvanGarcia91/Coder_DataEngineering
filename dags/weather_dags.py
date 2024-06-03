from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from weather_etl import etl_data

default_args = {
    'start_date': datetime(2024, 6, 2),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id="desafio3_pipeline",
    default_args=default_args,
    description='Agrega datos del clima en diferentes ciudades de Argentina',
    schedule_interval=timedelta(days=1),
    catchup=False
)

#task_1 = BashOperator(
#    task_id='first_task',
#    bash_command='echo Starting...'
#)


task_2 = PythonOperator(
    task_id='etl_data',
    python_callable=etl_data,
    dag=dag
)


#ask_3 = BashOperator(
#    task_id='last_task',
#    bash_command='echo Completed Process...'
#)


#task_1 >> task_2 >> task_3 
task_2