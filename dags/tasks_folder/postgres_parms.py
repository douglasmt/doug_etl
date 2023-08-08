localhost_server = 'host.docker.internal'
pg_conn=f"host={localhost_server} dbname=dvdrental user=postgres password=doug port='5432'"

pg_conn_id = "postgres"

select_tb = "SELECT customer_id, \
    store_id, first_name, last_name, \
    email, address_id, activebool, \
	create_date, last_update, active \
	FROM public.customer;"