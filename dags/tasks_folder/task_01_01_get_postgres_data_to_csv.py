import psycopg2
from . import postgres_parms
from . import postgres_query


# Building the parameters
i = 0
connection = psycopg2.connect(postgres_parms.pg_conn)
cursor = connection.cursor()


def run_query_with_psycopg_to_csv(ti):
    """
    Function to get data from postgres and generate the csv file
    :return:
    """
    try:
        print(postgres_parms.pg_conn)
        postgre_sql_select_query = postgres_query.select_tb

        cursor.execute(postgre_sql_select_query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()
        file_out_path = 'files/get_postgres_create_csv_output.csv'
        f_out = open(file_out_path, 'w')
        f_out.write(
            'customer_id,first_name,last_name,email'
        )
        import os
        print("Current Dir: " + os.getcwd())
        print("Print each row and it's columns values")
        for row in mobile_records:
            print(f"row {row}")
            print("customer_id = ", row[0], )
            print("store_id = ", row[1])
            print("first_name  = ", row[2], "\n")

            f_out.write(f"\n{row[0]}," +
                        f"{row[2]}," +
                        f"{row[3]}," +
                        f"{row[4]}"
                        )

        ti.xcom_push(key='my_key_customer', value=file_out_path)

        print("EVERYTHING WENT WELL")
    except (Exception, psycopg2.Error) as error:
        print("run_query_with_psycopg_to_csv:\n Error while fetching data from PostgreSQL ", error)
        raise Exception

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

