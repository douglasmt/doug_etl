localhost_server = 'host.docker.internal'
pg_conn = f"host={localhost_server} dbname=dvdrental user=postgres password=doug port='5432'"
# 	                Conn Id 	    Conn Type 	Host 	                Port 	Is Encrypted 	Is Extra Encrypted
# pg_conn_airflow = pg_conn_airflow	postgres	host.docker.internal	5432	False	        False

pg_conn_id = "postgres"
