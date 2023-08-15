from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from tasks_folder.pandas_task import *



with DAG(dag_id="dag_pandas_test", start_date=datetime(2023,1,1),
         schedule_interval='@daily',

         catchup=False) as dag:
    start_task = DummyOperator(task_id="process_start")

    
    join_dataframe = PythonOperator(task_id="join_pandas_dataframes",
                                    python_callable=pandas_join_dataframes)
    
    end_task = DummyOperator(task_id="process_end")

start_task >> join_dataframe >> end_task


