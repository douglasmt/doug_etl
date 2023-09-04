SELECT rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update
	FROM public.rental;

SELECT inventory_id, film_id, store_id, last_update
	FROM public.inventory;

SELECT film_id, title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, last_update, special_features, fulltext
	FROM public.film;

select * from customer

select 
r.rental_id, 
r.rental_date, 
r.return_date,
concat(c.first_name || ' ' ||  c.last_name), 
c.email,
f.film_id, f.title

	FROM public.rental r left join public.customer c on c.customer_id = r.customer_id
	left join public.inventory i on i.inventory_id = r.inventory_id
	left join public.film f on f.film_id = i.film_id
	



