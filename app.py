from flask import Flask
from app import db
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_swagger_ui import get_swaggerui_blueprint
from config import DevelopmentConfig
from config import TestingConfig

from routes import productBP
from routes import customeraccountBP
from routes import orderBP
from routes import customerBP

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


db = SQLAlchemy(app)
cache = Cache(app) 
limiter = Limiter(app, key_func=get_remote_address)



SWAGGER_URL = '/api/docs'  
API_URL = '/static/swagger.yaml'  
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "E-commerce API"
    }
)

def create_app(testing=False, config_name='DevelopmentConfig'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Tuckerstriker12@localhost/e_commerce_db'

    db.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    with app.app_context():
         print(app.config['SQLALCHEMY_DATABASE_URI']) 
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(productBP, url_prefix='/products')
    app.register_blueprint(customerBP, url_prefix='/customers')
    app.register_blueprint(orderBP, url_prefix='/orders')
    app.register_blueprint(customeraccountBP, url_prefix='/customeraccount')

    if testing:
        app.config.from_object('config.TestingConfig')  # Load testing config
    else:
        app.config.from_object('config.DevelopmentConfig')  # Load dev config
    
    return app

app.register_blueprint(productBP, url_prefix='/products')
app.register_blueprint(customeraccountBP, url_prefix='/customeraccount')
app.register_blueprint(orderBP, url_prefix='/orders')
app.register_blueprint(customerBP, url_prefix='/customers')
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL) 

if __name__ == '__main__':
    app.run(debug=True) # Run in development mode 