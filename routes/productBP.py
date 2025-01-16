from flask import Blueprint
from controllers.productController import create_product, get_product, update_product, delete_product
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

product_bp = Blueprint('product_bp', __name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})
limiter = Limiter(key_func=get_remote_address, default_limits=["100 per day"])

cache.init_app(product_bp)
limiter.init_app(product_bp)


product_bp.route('/products', methods=['POST'])(create_product)
product_bp.route('/products/<int:product_id>', methods=['GET'])(get_product)
product_bp.route('/products/<int:product_id>', methods=['PUT'])(update_product)
product_bp.route('/products/<int:product_id>', methods=['DELETE'])(delete_product)