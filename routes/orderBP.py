from flask import Blueprint
from controllers.orderController import create_order, get_order, update_order, delete_order
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


order_bp = Blueprint('order_bp', __name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})
limiter = Limiter(key_func=get_remote_address, default_limits=["100 per day"])

cache.init_app(order_bp)
limiter.init_app(order_bp)


order_bp.route('/orders', methods=['POST'])(create_order)
order_bp.route('/orders/<int:order_id>', methods=['GET'])(get_order)
order_bp.route('/orders/<int:order_id>', methods=['PUT'])(update_order)
order_bp.route('/orders/<int:order_id>', methods=['DELETE'])(delete_order)

