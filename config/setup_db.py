from tqdm.auto import tqdm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData


DB_URI = "postgresql://oahbrqsqfwprex:080de6cee2728457fd6d70612b99c01c9d5788a013c362ea1b126332dc825f92@ec2-3-208-157-78.compute-1.amazonaws.com:5432/dbrb9h946usn0k"


engine = create_engine(DB_URI)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()


def format_table():
    commands = [
        "drop table customer cascade",
        "drop table cart cascade",
        "drop table transaction cascade",
        "drop table brand cascade", 
        "drop table supplier cascade", 
        "drop table product cascade",
        "drop table sold_by cascade", 
        "drop table review cascade",
        "drop table customer_order cascade"
    ]

    for command in commands:
        try:
            connection.execute(command)
        except Exception as e:
            print(e)

def format_trigger():
    commands = [
        "drop trigger if exists increment_cart on customer_order",
        "drop trigger if exists decrement_cart on customer_order",
        "drop trigger if exists insert_cart_trigger on customer"
    ]

    for command in commands:
        try:
            connection.execute(command)
        except Exception as e:
            print(e)


def create_tables():
    from db_config import db
    db.create_all()


def create_triggers():
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
    UPDATE cart set amount=amount-(select price from product where old.p_id = product.p_id) where old.cart_id=cart.cart_id;
    UPDATE transaction set amount=(select amount from cart where old.cart_id=cart.cart_id) where old.cart_id=transaction.customer_id;
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

    connection.execute(statement_increment_cart)
    connection.execute(statement_decrement_cart)
    connection.execute(statement_init_cart)


def insert_data():
    with open("insert.sql") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line != ""]
        for line in tqdm(lines):
            connection.execute(line)


format_trigger()
format_table()
create_tables()
create_triggers()
insert_data()
