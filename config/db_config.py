from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_URI = "postgresql://oahbrqsqfwprex:080de6cee2728457fd6d70612b99c01c9d5788a013c362ea1b126332dc825f92@ec2-3-208-157-78.compute-1.amazonaws.com:5432/dbrb9h946usn0k"


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = "customer"
    customer_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.Date(), nullable=False)  # need to check
    billing_address = db.Column(db.String(200), nullable=False)
    shipping_address = db.Column(db.String(200), nullable=False)

    def __init__(self, customer_id, name, password, email, phone_no, dob, billing_address, shipping_address) -> None:
        self.customer_id = customer_id
        self.name = name
        self.password = password
        self.email = email
        self.phone_no = phone_no
        self.dob = dob
        self.billing_address = billing_address
        self.shipping_address = shipping_address


class Transaction(db.Model):
    __tablename__ = "transaction"
    transaction_id = db.Column(db.String(), primary_key=True)
    amount = db.Column(db.Integer(), nullable=False)
    mode = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.Integer(), db.ForeignKey(
        'customer.customer_id', ondelete='CASCADE'), nullable=False)

    def __init__(self, transaction_id, amount, mode, customer_id) -> None:
        self.transaction_id = transaction_id
        self.amount = amount
        self.mode = mode
        self.customer_id = customer_id


class Brand(db.Model):
    __tablename__ = "brand"
    brand_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100), nullable=False)

    def __init__(self, brand_id, name, website) -> None:
        self.brand_id = brand_id
        self.name = name
        self.website = website


class Supplier(db.Model):
    __tablename__ = "supplier"
    s_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, s_id, name, website, phone_no, email) -> None:
        self.s_id = s_id
        self.name = name
        self.website = website
        self.phone_no = phone_no
        self.email = email


class Cart(db.Model):
    __tablename__ = "cart"
    cart_id = db.Column(db.Integer(), primary_key=True)
    number_of_products = db.Column(db.Integer(), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)

    def __init__(self, cart_id, number_of_products, amount) -> None:
        self.cart_id = cart_id
        self.number_of_products = number_of_products
        self.amount = amount


class Sold_by(db.Model):
    __tablename__ = "sold_by"
    brand_id = db.Column(db.Integer(), db.ForeignKey(
        'brand.brand_id', ondelete='CASCADE'), primary_key=True)
    s_id = db.Column(db.Integer(), db.ForeignKey(
        'supplier.s_id', ondelete='CASCADE'), primary_key=True)

    def __init__(self, brand_id, s_id) -> None:
        self.brand_id = brand_id
        self.s_id = s_id


class Product(db.Model):
    __tablename__ = "product"
    p_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    brand_id = db.Column(db.Integer(), db.ForeignKey(
        'brand.brand_id', ondelete='CASCADE'), nullable=False)

    def __init__(self, p_id, name, description, price, brand_id) -> None:
        self.p_id = p_id
        self.name = name
        self.description = description
        self.price = price
        self.brand_id = brand_id


class Review(db.Model):
    __tablename__ = "review"

    date = db.Column(db.Date(), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    customer_id = db.Column(db.Integer(), db.ForeignKey(
        'customer.customer_id', ondelete='CASCADE'), primary_key=True)
    p_id = db.Column(db.Integer(), db.ForeignKey(
        'product.p_id', ondelete='CASCADE'), primary_key=True)

    def __init__(self, date, rating, description, customer_id, p_id) -> None:
        self.date = date
        self.rating = rating
        self.description = description
        self.customer_id = customer_id
        self.p_id = p_id


class Customer_order(db.Model):
    __tablename__ = "customer_order"
    cart_id = db.Column(db.Integer(), db.ForeignKey(
        'cart.cart_id', ondelete='CASCADE'), primary_key=True)
    p_id = db.Column(db.Integer(), db.ForeignKey(
        'product.p_id', ondelete='CASCADE'), primary_key=True)

    def __init__(self, cart_id, p_id) -> None:
        self.cart_id = cart_id
        self.p_id = p_id


if __name__ == "__main__":
    app.run()