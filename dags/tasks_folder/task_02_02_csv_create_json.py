import csv
import json


def run_transform_csv_to_json():
    """
    Function to process csv file and return json keys
    :return:
    """
    csv_in = "files/get_postgres_create_csv_output.csv"
    try:
        file_dict = {}
        list_in_dict = []
        i = 0

        with open(csv_in, 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                # print(row)
                list_in_dict.append(row)
                i += 1

        file_dict["PurchaseOrders"] = list_in_dict
        file_dict_final = json.dumps(file_dict)
        print(file_dict_final)
        with open("files/get_csv_create_json_output.json", 'w') as file:
            file.write(str(file_dict_final))
    except FileNotFoundError as ex:
        print(f"\n\nTASK: run_transform_csv_to_json\n Error reading the file:\n {csv_in} \nError:\n {ex} \n")
        raise FileNotFoundError
