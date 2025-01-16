from flask import request
from models.product import Product
from app import db # Import your Flask-SQLAlchemy instance
from utils.response import response_success, response_error

def create_product():
    try:
        data = request.get_json()
        # ... Data validation
        new_product = Product(**data)
        db.session.add(new_product)
        db.session.commit()
        return response_success(message='Product created successfully', data=new_product.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500

def get_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        return response_success(message='Product retrieved successfully', data=product.to_dict())
    except Exception as e:
        return response_error(message=str(e)), 500
    
def update_product(product_id):
    try:
        data = request.get_json()
        product = Product.query.get_or_404(product_id)
        product.update(**data)
        db.session.commit()
        return response_success(message='Product updated successfully', data=product.to_dict())
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500
    
def delete_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return response_success(message='Product deleted successfully')
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500
    
