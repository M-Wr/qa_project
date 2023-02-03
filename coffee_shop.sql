--	SQL Table within your database that contains order_id, customer_name, drink, size, extras, price,
CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(30),
    drink VARCHAR(30),
    size CHAR(3),
    extras VARCHAR(50), 
    price INTEGER
);

CREATE TABLE prices(
    drink_id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink VARCHAR(30),
    price FLOAT
);

