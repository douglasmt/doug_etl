import json
import psycopg2
import redis


'''
Download the JSON using the link below


https://drive.google.com/file/d/1zxB0lGMEYtB-STd0kNtvCGqcJeZP8juy/view?usp=share_link



Convert the JSON to CSV with the following columns:

po#, billing_name, billing_street, billing_city, billing_state, billing_zip, billing_country, items

Items format: PartNumber:Qty:Price | PartNumber2:Qty:Price


Save data into the database in a table
'''

def get_json_create_csv_output():
    f = open("..\\files\inputs\purchase_orders.json")
    obj = json.load(f)
    f_out = open('..\\files\outputs\get_json_create_csv_output.csv', 'w')
    f_out.write(
        'po#, billing_name, billing_street, billing_city, billing_state, billing_zip, billing_country, items'
        )



    i = 0
    countRedis = 0
    while i < len(obj["PurchaseOrders"]):
        #print(obj["PurchaseOrders"][i]['Address'][1]['Type'])
        
        if type(obj["PurchaseOrders"][i]['Items']['Item']) is list:
            j = 0  
            print(f"\nOrder {obj['PurchaseOrders'][i]['PurchaseOrderNo']}: ")
            while j < len(obj['PurchaseOrders'][i]['Items']['Item']):
                print(               
                    f"Part - {obj['PurchaseOrders'][i]['Items']['Item'][j]['PartNumber']} " +
                    f"Quantity - {obj['PurchaseOrders'][i]['Items']['Item'][j]['Quantity']} " +
                    f"USPrice - {obj['PurchaseOrders'][i]['Items']['Item'][j]['USPrice']} " 
                )
                k = 0
                while k < len(obj['PurchaseOrders'][i]['Address']):
                    if obj['PurchaseOrders'][i]['Address'][k]['Type'] == 'Billing':

                        # FILE

                        items_string = f"{obj['PurchaseOrders'][i]['Items']['Item'][j]['PartNumber']}:{obj['PurchaseOrders'][i]['Items']['Item'][j]['Quantity']}:{obj['PurchaseOrders'][i]['Items']['Item'][j]['USPrice']}"
                        
                        f_out.write(f"\n{obj['PurchaseOrders'][i]['PurchaseOrderNo']},"+
                            f"{obj['PurchaseOrders'][i]['Address'][k]['Name']},"+                        
                            f"{obj['PurchaseOrders'][i]['Address'][k]['Street']},"+                        
                            f"{obj['PurchaseOrders'][i]['Address'][k]['City']},"+                        
                            f"{obj['PurchaseOrders'][i]['Address'][k]['State']},"+                        
                            f"{obj['PurchaseOrders'][i]['Address'][k]['Zip']},"+                        
                            f"{obj['PurchaseOrders'][i]['Address'][k]['Country']},"+                        
                            items_string
                        )

                    k += 1
                j += 1

            print(f"\n")

        else:
            print(f"Order {obj['PurchaseOrders'][i]['PurchaseOrderNo']}: " +               
                f"Part - {obj['PurchaseOrders'][i]['Items']['Item']['PartNumber']} " +
                f"Quantity - {obj['PurchaseOrders'][i]['Items']['Item']['Quantity']} " +
                f"USPrice - {obj['PurchaseOrders'][i]['Items']['Item']['USPrice']} " 
            )
            k = 0
            while k < len(obj['PurchaseOrders'][i]['Address']):
                if obj['PurchaseOrders'][i]['Address'][k]['Type'] == 'Billing':

                    items_string = f"{obj['PurchaseOrders'][i]['Items']['Item']['PartNumber']}:{obj['PurchaseOrders'][i]['Items']['Item']['Quantity']}:{obj['PurchaseOrders'][i]['Items']['Item']['USPrice']}"

                    # File
                    f_out.write(f"\n{obj['PurchaseOrders'][i]['PurchaseOrderNo']},"+
                        f"{obj['PurchaseOrders'][i]['Address'][k]['Name']},"+                        
                        f"{obj['PurchaseOrders'][i]['Address'][k]['Street']},"+                        
                        f"{obj['PurchaseOrders'][i]['Address'][k]['City']},"+                        
                        f"{obj['PurchaseOrders'][i]['Address'][k]['State']},"+                        
                        f"{obj['PurchaseOrders'][i]['Address'][k]['Zip']},"+                        
                        f"{obj['PurchaseOrders'][i]['Address'][k]['Country']},"+                        
                        items_string
                    )
                k += 1

        i += 1


