import json
import psycopg2
from . import postgres_parms

# Building the parameters
i = 0 
count = 0
if count == 0:
    count +=1
if count == None:
    count = 0
    
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


