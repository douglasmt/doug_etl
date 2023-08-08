import csv, json
import redis


# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=1)

file_dict = {}
list_in_dict = []
i=0
with open("..\\files\outputs\get_json_create_csv_output.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        key_name = 'PurchaseOrder' + str(i)
        r.set(key_name, json.dumps(row))
        i += 1
