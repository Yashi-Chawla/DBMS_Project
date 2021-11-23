import datetime
from sqlalchemy import inspect, and_
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker


DB_URI = "postgresql://oahbrqsqfwprex:080de6cee2728457fd6d70612b99c01c9d5788a013c362ea1b126332dc825f92@ec2-3-208-157-78.compute-1.amazonaws.com:5432/dbrb9h946usn0k"


engine = create_engine(DB_URI)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

customer_table = Table('customer', metadata, autoload=True, autoload_with=engine)
transaction_table = Table('transaction', metadata, autoload=True, autoload_with=engine)
brand_table = Table('brand', metadata, autoload=True, autoload_with=engine)
suppler_table = Table('supplier', metadata, autoload=True, autoload_with=engine)
cart_table = Table('cart', metadata, autoload=True, autoload_with=engine)
sold_by_table = Table('sold_by', metadata, autoload=True, autoload_with=engine)
product_table = Table('product', metadata, autoload=True, autoload_with=engine)
review_table = Table('review', metadata, autoload=True, autoload_with=engine)
customer_order_table = Table('customer_order', metadata, autoload=True, autoload_with=engine)

def verify_credentials(email, password):
    query = customer_table.select().where(and_(customer_table.c.email == email, customer_table.c.password == password))
    result = connection.execute(query).fetchall()
    if len(result):
        user_id = result[0][0]
        return True, user_id
    else:
        return False, None


def get_username(user_id):
    query = customer_table.select().where(customer_table.c.customer_id == user_id)
    result = connection.execute(query).fetchall()
    if len(result):
        return result[0][1]
    else:
        return None

def get_product_details_from_id(product_id):
    query = product_table.select().where(product_table.c.p_id == product_id)
    result = connection.execute(query).fetchall()
    if result:
        return result[0]
    else:
        return None


def get_cart_for_user(user_id):
    query = cart_table.select().where(cart_table.c.cart_id == user_id)
    result = connection.execute(query).fetchall()
    if result:
        num_products = result[0][1]
        total_amount = result[0][2]
        query = customer_order_table.select().where(customer_order_table.c.cart_id == user_id)
        result = connection.execute(query).fetchall()
        product_ids = [p[1] for p in result]
        cart_details = [get_product_details_from_id(p) for p in product_ids]
        return cart_details, total_amount, num_products
    return None, None, None


def get_all_products():
    query = product_table.select()
    result = connection.execute(query).fetchall()
    if result:
        return result
    else:
        return None


def add_product_to_order(user_id, product_id):
    query = customer_order_table.insert().values(cart_id=user_id, p_id=product_id)
    try:
        connection.execute(query)
        return True
    except:
        return False


def get_reviews_for_product(product_id):
    query = review_table.select().where(review_table.c.p_id == product_id)
    result = connection.execute(query).fetchall()
    if result:
        result = list(map(lambda x: (x[0], x[1], x[2]), result))
        result.sort(key=lambda x:x[0], reverse=True)
        return result
    else:
        return None


def add_review(product_id, user_id, rating, review, date):
    query = review_table.insert().values(p_id=product_id, customer_id=user_id, rating=rating, description=review, date=date)
    try:
        connection.execute(query)
        return True
    except:
        return False

# def create_user(customer_id, name, password, email, phone_no, dob, billing_address, shipping_address):
#     query = customer_table.insert().values(customer_id=customer_id, name=name, password=password, email=email, phone_no=phone_no, dob=dob, billing_address=billing_address, shipping_address=shipping_address)
#     connection.execute(query)
