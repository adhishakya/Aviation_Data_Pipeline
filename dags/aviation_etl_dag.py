from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
from aviation_package.get_data import get_aviation_data
from aviation_package.db_operation import insert_aviation_data
from aviation_package.data_cleaning import insert_cleaned_aviation_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'aviation_dag',
    default_args = default_args,
    schedule_interval = timedelta(hours = 1),
    catchup =  False
):
    fetch_aviation_data = PythonOperator(
        task_id = 'get_aviation_data',
        python_callable = get_aviation_data,
        provide_context = True
    )

    insert_aviation_data_in_database = PythonOperator(
        task_id = 'insert_aviation_data',
        python_callable = insert_aviation_data,
        provide_context = True
    )

    insert_cleaned_aviation_data_in_database = PythonOperator(
        task_id = 'insert_cleaned_aviation_data',
        python_callable = insert_cleaned_aviation_data
    )
    
    fetch_aviation_data >> insert_aviation_data_in_database >> insert_cleaned_aviation_data_in_database
