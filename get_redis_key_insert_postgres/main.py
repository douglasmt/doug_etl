import redis, redis_conn
import json
import psycopg2, postgres_parms
import parameters_app1


# Connect to Redis
r = redis.Redis(host=redis_conn.host, port=6379, db=1)

# Connect to postgres
conn = psycopg2.connect(postgres_parms.pg_conn)

# Building the parameters
redis_keys = parameters_app1.parameters_keys
i = 0 
cur = conn.cursor()
cur.execute(postgres_parms.check_tb)
count = 0
cur.execute(postgres_parms.select_tb_index)
count = cur.fetchone()[0]
if count == 0:
    count +=1
if count == None:
    count = 0
    
# Retrieve stored data from Redis and deserialize it back into JSON
while i < redis_keys:        
    get_key = str(parameters_app1.key_redis#+ str(f'{i}')
                  )
    print('getting: ' + get_key)
    retrieved_data_string = r.get(get_key)
    retrieved_data = json.loads(retrieved_data_string)
    print(retrieved_data)
    i += 1

    cur.execute(
    postgres_parms.insert_tb, 
    (count, 
     retrieved_data['name'], 
     retrieved_data['age'], 
     retrieved_data['email']
     )
     )
    conn.commit()



