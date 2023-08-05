import json
import psycopg2, postgres_parms
import parameters_app1
import redis, redis_conn


# Connect to postgres
conn = psycopg2.connect(postgres_parms.pg_conn)

# Connect to Redis
r = redis.Redis(host=redis_conn.host, port=6379, db=1)

# Building the parameters
i = 0 
cur = conn.cursor()
count = 0
result_sql = cur.execute(postgres_parms.select_tb)
count = cur.fetchone()[0]
if count == 0:
    count +=1
if count == None:
    count = 0
    
if __name__ == "__main__":
    try:
        connection = psycopg2.connect(postgres_parms.pg_conn)
        cursor = connection.cursor()
        postgreSQL_select_Query = postgres_parms.select_tb

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        json_out_schema = ['customer_id', 'first_name', 'last_name', 'email']
        for row in mobile_records:
            print("customer_id = ", row[0], )
            print("store_id = ", row[1])
            print("first_name  = ", row[2], "\n")
            
            key_name = 'DvdRCustomer' + str(i)
            row_select = [row[0], row[2], row[3], row[4]]
            row_json = dict(list(zip(json_out_schema, row_select)))
            print(row_json)
            r.set(key_name, json.dumps(row_json))

            i += 1


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")