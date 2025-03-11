from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
from get_data import get_aviation_data
from db_operation import insert_aviation_data

default_args = {
    'owner': 'airflow',
    'start_date': ''
}

with DAG(
    'aviation_dag',
    default_args = default_args,
    schedule = timedelta(hours = 1),
    catchup =  False
):
    get_aviation_data = PythonOperator(
        task_id = 'get_aviation_data',
        python_callable = get_aviation_data()
    )

    insert_aviation_data = PythonOperator(
        task_id = 'insert_aviation_data',
        python_callable = insert_aviation_data()
    )
    
    get_aviation_data >> insert_aviation_data
