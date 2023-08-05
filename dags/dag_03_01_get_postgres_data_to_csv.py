from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
import psycopg2, postgres_parms
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

import json
from pandas import json_normalize


from datetime import datetime

def run_query_with_psycopg():
        try:
            print(postgres_parms.pg_conn)
            connection = psycopg2.connect(postgres_parms.pg_conn)
            cursor = connection.cursor()
            postgreSQL_select_Query = postgres_parms.select_tb

            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from mobile table using cursor.fetchall")
            mobile_records = cursor.fetchall()

            f_out = open('files/get_postgres_create_csv_output.csv', 'w')
            f_out.write(
                'customer_id, first_name, last_name, email'
            )
            import os
            print("Current Dir: " + os.getcwd())              
            print("Print each row and it's columns values")
            for row in mobile_records:
                print("customer_id = ", row[0], )
                print("store_id = ", row[1])
                print("first_name  = ", row[2], "\n")
                

                f_out.write(f"\n{row[0]},"+
                    f"{row[2]},"+
                    f"{row[3]},"+
                    f"{row[4]}"
                )
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

with DAG('dag_03_01_get_postgres_data_to_csv', start_date=datetime(2023,1,1),
         schedule_interval='@daily', 
         catchup=False # means that the DAG was not triggered since the start date
         ) as dag:
    
    select_dvdrental_table = PythonOperator(
        task_id='select_dvdrental_table',
        python_callable=run_query_with_psycopg
    )


select_dvdrental_table