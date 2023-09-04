from airflow import DAG
from datetime import datetime
from tasks_folder import postgres_parms

from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG('dag_01_sql_selection',
         start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False
         ) as dag:
    task_01_select = PostgresOperator(
        task_id='task_selection_table',
        postgres_conn_id="pg_conn_airflow",
        sql="SELECT customer_id, \
    store_id, first_name, last_name, \
    email, address_id, activebool, \
    create_date, last_update, active \
    FROM public.customer \
    --where last_update  = \'2023-08-09 11:52:49.123419\' \
    order by customer_id ;"
        # , parameters={'last_update' : '2023-08-09 11:52:49.123419'}

    )
