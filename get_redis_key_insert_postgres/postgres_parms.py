pg_conn="host=localhost dbname=DataWarehouseX user=postgres password=doug port='5432'"

check_tb = """
    CREATE TABLE IF NOT EXISTS public.clients_json(
    id integer PRIMARY KEY,
    name text,
    age integer,
    email text
)
"""

select_tb_index = 'SELECT max(id) FROM public.clients_json'

insert_tb = "INSERT INTO public.clients_json VALUES (%s, %s, %s, %s)"