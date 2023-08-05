from airflow import DAG

from datetime import datetime

with DAG('dag_01_get_json_create_csv', start_date=datetime(2023,1,1),
         schedule_interval='@daily', 
         catchup=False # means that the DAG was not triggered since the start date
         ) as dag:
    None