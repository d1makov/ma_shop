create table products (
	id serial primary key,
	name varchar(255),
	price integer,
	image bytea,
	category_id integer references product_categories(id) on delete set null,
	deleted boolean default false
);
