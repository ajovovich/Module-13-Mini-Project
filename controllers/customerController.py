from flask import request
from app import db
from models.customer import Customer
from models.customeraccount import CustomerAccount
from utils.response import response_success, response_error

def create_customer():
    try:
        data = request.get_json()
        new_customer = Customer(**data)
        db.session.add(new_customer)
        db.session.commit()
        return response_success(message='Customer created successfully', data=new_customer.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500

def get_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        return response_success(message='Customer retrieved successfully', data=customer.to_dict())
    except Exception as e:
        return response_error(message=str(e)), 500
    
def update_customer(customer_id):
    try:
        data = request.get_json
        customer = Customer.query.get_or_404(customer_id)
        customer.update(**data)
        db.session.commit()
        return response_success(message='Customer updated successfully', data=customer.to_dict())
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500
    
def delete_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return response_success(message='Customer deleted successfully')
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500
    
    