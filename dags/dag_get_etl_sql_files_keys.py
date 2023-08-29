"""
DAG dag_get_etl_sql_files_keys:
 - Extracts data from Postgres table
 - writes data to a csv file
 - writes data to a json file
 - creates redis keys with the json file

"""
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

import psycopg2
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

from tasks_folder.task_03_01_get_postgres_data_to_csv import run_query_with_psycopg
from tasks_folder.task_02_01_csv_create_json import run_transform_csv_to_json
from tasks_folder.task_02_02_csv_create_key_redis import run_csv_create_key_redis

import json
from pandas import json_normalize

from datetime import datetime

with DAG('dag_get_etl_sql_files_keys', start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False  # means that the DAG was not triggered since the start date
         ) as dag:
    dummy_start = DummyOperator(task_id='process_start')

    select_dvdrental_table = PythonOperator(
        task_id='select_dvdrental_table',
        python_callable=run_query_with_psycopg
    )

    transform_csv_to_json = PythonOperator(
        task_id='transform_csv_to_json',
        python_callable=run_transform_csv_to_json
    )

    csv_create_key_redis = PythonOperator(
        task_id='csv_create_key_redis',
        python_callable=run_csv_create_key_redis
    )

    dummy_end = DummyOperator(task_id='process_end')

dummy_start >> select_dvdrental_table >> [transform_csv_to_json, csv_create_key_redis] >> dummy_end
