select_tb = "SELECT customer_id, \
    store_id, first_name, last_name, \
    email, address_id, activebool, \
    create_date, last_update, active \
    FROM public.customer \
    --where last_update  = \'2023-08-09 11:52:49.123419\' \
    order by customer_id ;"

# now() - interval '1 week'

select_rental_data = """select 
r.rental_id, 
r.rental_date, 
r.return_date,
concat(c.first_name || ' ' ||  c.last_name) as customer_name, 
c.email,
f.film_id, f.title
 FROM public.rental r left join public.customer c on c.customer_id = r.customer_id
 left join public.inventory i on i.inventory_id = r.inventory_id
 left join public.film f on f.film_id = i.film_id
 order by rental_id"""
