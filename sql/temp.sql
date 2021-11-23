-- Trigger 1
CREATE OR REPLACE FUNCTION increment() RETURNS TRIGGER AS
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
     EXECUTE PROCEDURE increment();
    
--Trigger 2 
CREATE OR REPLACE FUNCTION decrement() RETURNS TRIGGER AS
$$
BEGIN
  UPDATE cart set number_of_products=number_of_products-1 where old.cart_id=cart.cart_id;
  UPDATE cart set amount=amount-(select price from product where old.p_id = product.p_id) where old.cart_id=cart.cart_id;
    RETURN new;
END;
$$
language plpgsql;

CREATE TRIGGER decrement_cart
    AFTER DELETE ON customer_order
    FOR EACH ROW
    EXECUTE PROCEDURE decrement();

--Trigger 3 (cart-id, number_of_products,amount)
CREATE OR REPLACE FUNCTION insert_cart() RETURNS TRIGGER AS 
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
EXECUTE PROCEDURE insert_cart();