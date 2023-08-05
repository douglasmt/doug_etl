pg_conn="host=localhost dbname=dvdrental user=postgres password=doug port='5432'"

select_tb = "SELECT customer_id, \
    store_id, first_name, last_name, \
    email, address_id, activebool, \
	create_date, last_update, active \
	FROM public.customer;"
    # \
	#where customer_id = 1;"

#insert_tb = "INSERT INTO public.clients_json VALUES (%s, %s, %s, %s)"