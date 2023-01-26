from datetime import datetime
from app_factory import db
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ordered_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow())
    delivered_date = db.Column(db.DateTime, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


