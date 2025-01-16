from flask import Blueprint
from utils.auth import token_required, admin_required
from controllers.customeraccountController import create_customer_account, get_customer_account, update_customer_account, delete_customer_account
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

customeraccount_bp = Blueprint('customeraccount_bp', __name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})
limiter = Limiter(key_func=get_remote_address, default_limits=["100 per day"])

cache.init_app(customeraccount_bp)
limiter.init_app(customeraccount_bp)


@customeraccount_bp.route('/customeraccount', methods=['POST'])
@token_required
@admin_required
@cache.cached(timeout=60)
@limiter.limit("100 per day")
def create_account(current_user):
    return create_customer_account()

@customeraccount_bp.route('/customeraccount/<int:customeraccount_id>', methods=['GET'])
@token_required
@admin_required
@cache.cached(timeout=60)
@limiter.limit("100 per day")
def get_account(current_user, customeraccount_id):
    return get_customer_account(customeraccount_id)

@customeraccount_bp.route('/customeraccount/<int:customeraccount_id>', methods=['PUT'])
@token_required
@admin_required
@cache.cached(timeout=60)
@limiter.limit("100 per day")
def update_account(current_user, customeraccount_id):
    return update_customer_account(customeraccount_id)

@customeraccount_bp.route('/customeraccount/<int:customeraccount_id>', methods=['DELETE'])
@token_required
@admin_required
@cache.cached(timeout=60)
@limiter.limit("100 per day")
def delete_account(current_user, customeraccount_id):
    return delete_customer_account(customeraccount_id)