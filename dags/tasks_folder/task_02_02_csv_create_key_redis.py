import csv, json
import redis


# Connect to Redis
r = redis.Redis(host='25-doug_etl-redis-1', port=6379, db=1)

def run_csv_create_key_redis():
    i=0
    with open("files/get_postgres_create_csv_output.csv", 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            key_name = 'PurchaseOrder' + str(i)
            print(str(key_name) + ': ' + str(row))
            r.set(key_name, json.dumps(row))
            i += 1