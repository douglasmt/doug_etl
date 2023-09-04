from airflow import DAG
from datetime import datetime

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator

with DAG('dag_02_tests',
         start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    dummy_start = DummyOperator(task_id='start_tests')

    task_test = BashOperator(
        task_id='test_python_code',
        bash_command="python /opt/airflow/dags/tasks_folder/unit_test_testes.py -v"# "echo \"hello world\";pwd;ls"#

    )

    dummy_end = DummyOperator(task_id='end_of_tests')

dummy_start >> task_test >> dummy_end
