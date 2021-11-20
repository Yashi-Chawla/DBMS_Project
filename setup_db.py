from sqlalchemy import inspect, and_
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker


DB_URI = "postgresql://oahbrqsqfwprex:080de6cee2728457fd6d70612b99c01c9d5788a013c362ea1b126332dc825f92@ec2-3-208-157-78.compute-1.amazonaws.com:5432/dbrb9h946usn0k"


engine = create_engine(DB_URI)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

statement_increment_cart = '''CREATE OR REPLACE FUNCTION increment() RETURNS TRIGGER AS
$$
BEGIN
  UPDATE cart set number_of_products=number_of_products+1 where new.cart_id=cart.cart_id;
  UPDATE cart set amount=amount+(select price from product where new.p_id = product.p_id) where new.cart_id=cart.cart_id;
  UPDATE transaction set amount=(select amount from cart where new.cart_id=cart.cart_id) where new.cart_id=transaction.customer_id;
    RETURN new;
END;
$$
language plpgsql;

CREATE TRIGGER increment_cart
     AFTER INSERT ON customer_order
     FOR EACH ROW
     EXECUTE PROCEDURE increment();'''


statement_decrement_cart = '''CREATE OR REPLACE FUNCTION decrement() RETURNS TRIGGER AS
$$
BEGIN
  UPDATE cart set no_of_products=no_of_products-1 where old.cart_id=cart.cart_id;
  UPDATE cart set total_amount=total_amount-(select price from product where old.p_id = product.p_id) where old.cart_id=cart.cart_id;
  UPDATE transaction set amount=(select total_amount from cart where old.cart_id=cart.cart_id) where old.cart_id=transaction.customer_id;
    RETURN new;
END;
$$
language plpgsql;

CREATE TRIGGER decrement_cart
    AFTER DELETE ON customer_order
    FOR EACH ROW
    EXECUTE PROCEDURE decrement();'''

statement_init_cart = '''CREATE OR REPLACE FUNCTION insert_cart() RETURNS TRIGGER AS 
$$
BEGIN
INSERT INTO CART(cart_id,number_of_products,amount) VALUES (new.customer_id,0,0);
RETURN NEW;
END;
$$
language plpgsql;

CREATE TRIGGER insert_cart_trigger
AFTER INSERT ON customer
FOR EACH ROW 
EXECUTE PROCEDURE insert_cart();'''

# all insert statements here itself?

connection.execute(statement_increment_cart)
connection.execute(statement_decrement_cart)
connection.execute(statement_init_cart)
