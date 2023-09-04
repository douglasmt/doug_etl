import psycopg2
from . import postgres_parms
from . import postgres_query

# Building the parameters
i = 0
connection = psycopg2.connect(postgres_parms.pg_conn)
cursor = connection.cursor()


def run_query_with_psycopg_to_csv_rentals_data(ti):
    """
    Function to get data from postgres and generate the csv file
    :return:
    """
    try:
        print(postgres_parms.pg_conn)
        postgres_sql_select_query = postgres_query.select_rental_data

        cursor.execute(postgres_sql_select_query)
        print("Selecting rows from rentals/customer/movie tables using cursor.fetchall")
        rental_records = cursor.fetchall()
        rental_path = 'files/get_rentals_csv_output.csv'
        f_out = open(rental_path, 'w')
        f_out.write(
            'rental_id,rental_date,return_date,customer_name,email,film_id,title'
        )
        import os
        print("Current Dir: " + os.getcwd())
        print("Print each row and it's columns values")
        for row in rental_records:
            # print(f"row {row}")
            print("rental_id = ", row[0], "rental_date = ", row[1]
                  , "return_date  = ", row[2], "customer_name  = ", row[3]
                  , "email  = ", row[4], "film_id  = ", row[5], "title  = ", row[6],
                  "\n")
            # row_write = ''
            row_write = ','.join([str(col) for col in row])
            print(row_write)
            f_out.write(
                f"\n{row_write}"
            )
        ti.xcom_push(key='my_key_rental', value=rental_path)

        print("EVERYTHING WENT WELL")
    except (Exception, psycopg2.Error) as error:
        print("run_query_with_psycopg_to_csv_rentals_data:\n Error while fetching data from PostgreSQL ", error)
        raise Exception

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
