from website import db
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    
    # Relationship to Cart (items that user adds)
    cart_items = db.relationship('CartItem', backref='user', lazy=True)
    
    # Relationship to Orders (when a user places an order)
    orders = db.relationship('Order', backref='user', lazy=True)

# Products model
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    reviews = db.Column(db.Integer, nullable=False)

    # Relationship to CartItem (products in the user's cart)
    cart_items = db.relationship('CartItem', backref='products', lazy=True)

    def __repr__(self):
        return f"<Product {self.name}>"

# CartItem model (represents a user's cart items)
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    
    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Foreign key to Product
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

# Order model (when the user places an order)
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    
    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to CartItems (products that belong to this order)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

# OrderItem model (represents individual items within an order)
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Foreign key to Order
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    
    # Foreign key to Product
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
