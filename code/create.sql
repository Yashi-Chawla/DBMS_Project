drop database shopping;
create database shopping;

\c shopping

CREATE TABLE customer
(
  customer_id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email_id VARCHAR(50) NOT NULL,
  phone_no char(10) NOT NULL,
  dob DATE NOT NULL,
  billing_address VARCHAR(200) NOT NULL,
  shipping_address VARCHAR(200) NOT NULL,
  PRIMARY KEY (customer_id)
);

CREATE TABLE transaction
(
  transaction_id char(11) NOT NULL,
  amount FLOAT NOT NULL,
  mode VARCHAR(50) NOT NULL,
  customer_id INT NOT NULL,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE brand
(
  brand_id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  website VARCHAR(100),
  PRIMARY KEY (brand_id)
);

CREATE TABLE supplier
(
  s_id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  website VARCHAR(200),
  phone_no char(10) NOT NULL,
  email VARCHAR(50),
  PRIMARY KEY (s_id)
);

CREATE TABLE cart
(
  cart_id INT NOT NULL,
  no_of_products INT NOT NULL,
  -- delivery_date DATE NOT NULL DEFAULT CURRENT_DATE+INTERVAL'1 day',
  total_amount FLOAT NOT NULL,
  PRIMARY KEY (cart_id),
  FOREIGN KEY (cart_id) REFERENCES customer(customer_id)
);

CREATE TABLE sold_by
(
  brand_id INT NOT NULL,
  s_id INT NOT NULL,
  FOREIGN KEY (brand_id) REFERENCES brand(brand_id),
  FOREIGN KEY (s_id) REFERENCES supplier(s_id)
);

CREATE TABLE product
(
  p_id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(200) NOT NULL,
  price FLOAT NOT NULL,
  brand_id INT NOT NULL,
  PRIMARY KEY (p_id),
  FOREIGN KEY (brand_id) REFERENCES brand(brand_id)
);

CREATE TABLE review
(
  date DATE NOT NULL,
  rating INT NOT NULL,
  description VARCHAR(200) NOT NULL,
  customer_id INT NOT NULL,
  p_id INT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
  FOREIGN KEY (p_id) REFERENCES product(p_id)
);

CREATE TABLE customer_order
(
  cart_id INT NOT NULL,
  p_id INT NOT NULL,
  FOREIGN KEY (cart_id) REFERENCES cart(cart_id),
  FOREIGN KEY (p_id) REFERENCES product(p_id)
);

-- Triggers to make
--1. insert into order table(cart_id, p_id, should reflect in total amount of that cart_id in table cart, and increment of no of products)
--2. delete from order table 1. total amount-that product price, 2. number of products decrement
--3. insert into user. inserts a row into cart(default)

-- Trigger 1
CREATE OR REPLACE FUNCTION increment() RETURNS TRIGGER AS
$$
BEGIN
  UPDATE cart set no_of_products=no_of_products+1 where new.cart_id=cart.cart_id;
  UPDATE cart set total_amount=total_amount+(select price from product where new.p_id = product.p_id) where new.cart_id=cart.cart_id;
  UPDATE transaction set amount=(select total_amount from cart where new.cart_id=cart.cart_id) where new.cart_id=transaction.customer_id;
  -- UPDATE cart set delivery_date=delivery_date+INTERVAL'1 day' where cart.cart_id=new.cart_id;
    RETURN new;
END;
$$
language plpgsql;

CREATE TRIGGER increment_cart
     AFTER INSERT ON customer_order
     FOR EACH ROW
     EXECUTE PROCEDURE increment();
    
--Trigger 3 (cart-id, no_of_products,total_amount)
CREATE OR REPLACE FUNCTION insert_cart() RETURNS TRIGGER AS 
$$
BEGIN
INSERT INTO CART(cart_id,no_of_products,total_amount) VALUES (new.customer_id,0,0);
RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER insert_cart_trigger
AFTER INSERT ON customer
FOR EACH ROW 
EXECUTE PROCEDURE insert_cart();

CREATE OR REPLACE FUNCTION decrement() RETURNS TRIGGER AS
$$
BEGIN
  UPDATE cart set no_of_products=no_of_products-1 where new.cart_id=cart.cart_id;
  UPDATE cart set total_amount=total_amount-(select price from product where new.p_id = product.p_id) where new.cart_id=cart.cart_id;
    RETURN new;
END;
$$
language plpgsql;

CREATE TRIGGER decrement_cart
    AFTER DELETE ON customer_order
    FOR EACH ROW
    EXECUTE PROCEDURE decrement();

