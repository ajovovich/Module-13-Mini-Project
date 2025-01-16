from models.product import Product
from app import db

def create_product(data):
    try:
        new_product = Product(**data)
        db.session.add(new_product)
        db.session.commit()
        return new_product
    except Exception as e:
        db.session.rollback()
        raise e

def get_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        return product
    except Exception as e:
        raise e
    
def update_product(product_id, data):
    try:
        product = Product.query.get_or_404(product_id)
        product.update(**data)
        db.session.commit()
        return product
    except Exception as e:
        db.session.rollback()
        raise e

def delete_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    
def get_products():
    try:
        products = Product.query.all()
        return products
    except Exception as e:
        raise e