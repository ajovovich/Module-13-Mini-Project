from flask import request
from app import db
from models.order import Order
from utils.response import response_success, response_error

def create_order():
    try:
        data = request.get_json()
        new_order = Order(**data)
        db.session.add(new_order)
        db.session.commit()
        return response_success(message='Order created successfully', data=new_order.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500

def get_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        return response_success(message='Order retrieved successfully', data=order.to_dict())
    except Exception as e:
        return response_error(message=str(e)), 500

def update_order(order_id):
    try:
        data = request.get_json()
        order = Order.query.get_or_404(order_id)
        order.update(**data)
        db.session.commit()
        return response_success(message='Order updated successfully', data=order.to_dict())
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500

def delete_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return response_success(message='Order deleted successfully')
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500
    
