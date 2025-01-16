from models.customeraccount import CustomerAccount
from flask import request
from app import db
from utils.response import response_success, response_error

def create_customeraccount():
    try:
        data = request.get_json()
        new_customeraccount = CustomerAccount(**data)
        db.session.add(new_customeraccount)
        db.session.commit()
        return response_success(message='Customer account created successfully', data=new_customeraccount.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500

def get_customeraccount(customeraccount_id):
    try:
        customeraccount = CustomerAccount.query.get_or_404(customeraccount_id)
        return response_success(message='Customer account retrieved successfully', data=customeraccount.to_dict())
    except Exception as e:
        return response_error(message=str(e)), 500
    
def update_customeraccount(customeraccount_id):
    try:
        data = request.get_json
        customeraccount = CustomerAccount.query.get_or_404(customeraccount_id)
        customeraccount.update(**data)
        db.session.commit()
        return response_success(message='Customer account updated successfully', data=customeraccount.to_dict())
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500

def delete_customeraccount(customeraccount_id):
    try:
        customeraccount = CustomerAccount.query.get_or_404(customeraccount_id)
        db.session.delete(customeraccount)
        db.session.commit()
        return response_success(message='Customer account deleted successfully')
    except Exception as e:
        db.session.rollback()
        return response_error(message=str(e)), 500
    
def get_customeraccounts():
    try:
        customeraccounts = CustomerAccount.query.all()
        return response_success(message='Customer accounts retrieved successfully', data=[customeraccount.to_dict() for customeraccount in customeraccounts])
    except Exception as e:
        return response_error(message=str(e)), 500

def get_customeraccounts_by_customer_id(customer_id):
    try:
        customeraccounts = CustomerAccount.query.filter_by(customer_id=customer_id).all()
        return response_success(message='Customer accounts retrieved successfully', data=[customeraccount.to_dict() for customeraccount in customeraccounts])
    except Exception as e:
        return response_error(message=str(e)), 500
    