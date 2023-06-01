-- SQL-команды для создания таблиц

create table employees
(
employee_id int PRIMARY KEY,
first_name varchar(20) not NULL,
last_name varchar(20) not NULL,
title varchar(20) not NULL,
birth_date date,
notes text
)

create table customers
(
customer_id varchar(20) not NULL UNIQUE,
company_name varchar(30) not NULL,
contact_name varchar(20) not NULL
)

create table orders
(
order_id int PRIMARY KEY,
customer_id varchar(20) REFERENCES customers(customer_id),
employee_id int REFERENCES employees(employee_id) not NULL,
order_date date,
ship_city varchar(30) not NULL
)
