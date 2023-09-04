import csv
import json

import redis
from tasks_folder import redis_conn

# Connect to Redis
r = redis.Redis(host=redis_conn.host, port=6379, db=1)


def run_csv_create_key_redis(ti):
    """
    Function to generate Redis keys from the csv file
    :return:
    """
    print(ti.xcom_pull(key='my_key_customer', task_ids='select_customers_table'))

    csv_in = ti.xcom_pull(key='my_key_customer', task_ids='select_customers_table')

    try:
        i = 0
        with open(csv_in, 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                key_name = "Customer" + str(i)

                print(str(key_name) + ':' + str(row))
                r.set(key_name, json.dumps(row))
                i += 1
    except FileNotFoundError as file_not_found:
        print(f"\n\nTASK: run_csv_create_key_redis\n Error reading the file:\n {csv_in} \nError:\n {file_not_found} \n")
        raise FileNotFoundError
    except ConnectionError as connection_error:
        raise ConnectionError('Connection unsuccessful: \n' + str(connection_error))


def run_csv_create_rental_key_redis(ti):
    """
    Function to generate Redis keys from the csv file
    :return:
    """
    print(ti.xcom_pull(key='my_key_rental', task_ids='select_rentals_data'))

    csv_in = ti.xcom_pull(key='my_key_rental', task_ids='select_rentals_data')

    try:
        i = 0
        with open(csv_in, 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                key_name = "Rental" + str(i)

                print(str(key_name) + ':' + str(row))
                r.set(key_name, json.dumps(row))
                i += 1
    except FileNotFoundError as file_not_found:
        print(f"\n\nTASK: run_csv_create_rental_key_redis\n Error reading the file:\n {csv_in} \nError:\n {file_not_found} \n")
        raise FileNotFoundError
    except ConnectionError as connection_error:
        raise ConnectionError('Connection unsuccessful: \n' + str(connection_error))
