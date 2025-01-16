from flask import Blueprint
from controllers.customerController import create_customer, get_customer, update_customer, delete_customer
from utils.auth import admin_required
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

customer_bp = Blueprint('customer_bp', __name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})
limiter = Limiter(key_func=get_remote_address, default_limits=["100 per day"])

cache.init_app(customer_bp)
limiter.init_app(customer_bp)

@customer_bp.route('/customer', methods=['POST'])
@admin_required
@cache.cached(timeout=60)
@limiter.limit("100 per day")
def create_customer_route():
    return create_customer()

@customer_bp.route('/customer/<int:customer_id>', methods=['GET'])
@admin_required
@cache.cached(timeout=60)
@limiter.limit("100 per day")
def get_customer_route(customer_id):
    return get_customer(customer_id)

@customer_bp.route('/customer/<int:customer_id>', methods=['PUT'])
@admin_required
@cache.cached(timeout=60)
@limiter.limit("100 per day")
def update_customer_route(customer_id):
    return update_customer(customer_id)

@customer_bp.route('/customer/<int:customer_id>', methods=['DELETE'])
@admin_required
@cache.cached(timeout=60)
@limiter.limit("100 per day")
def delete_customer_route(customer_id):
    return delete_customer(customer_id)

