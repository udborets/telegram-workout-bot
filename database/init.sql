-- DROP SCHEMA public;
-- CREATE DATABASE telegram-workout-bot;
\c telegram-workout-bot;


COMMENT ON SCHEMA public IS 'standard public schema';
-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	id int8 NOT NULL PRIMARY KEY,
	telegram_chat_id int8 NOT NULL,
	telegram_name text NULL,
	current_weight numeric NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NOT NULL,
	CONSTRAINT telegram_chat_id_unique UNIQUE (telegram_chat_id),
);


-- public.products definition

-- Drop table

-- DROP TABLE public.products;

CREATE TABLE public.products (
	id int8 NOT NULL,
	"name" text NOT NULL,
	grams_per_serving numeric NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NOT NULL,
	protein_per_100_grams numeric NULL,
	fats_per_100_grams numeric NULL,
	carbs_per_100_grams numeric NULL,
	calories_per_100_grams numeric NULL,
	telegram_chat_id int8 NOT NULL,
	CONSTRAINT products_pk PRIMARY KEY (id),
	CONSTRAINT telegram_chat_id_fk FOREIGN KEY (telegram_chat_id) REFERENCES public.users(telegram_chat_id)
);


-- public.consumed_products definition

-- Drop table

-- DROP TABLE public.consumed_products;

CREATE TABLE public.consumed_products (
	id int8 NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NOT NULL,
	product_id int8 NOT NULL,
	CONSTRAINT consumed_products_pk PRIMARY KEY (id),
	CONSTRAINT comsumed_product_product_id_fk FOREIGN KEY (product_id) REFERENCES public.products(id)
);