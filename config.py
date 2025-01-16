class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Tuckerstriker12@127.0.0.1:3306/e_commerce_db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True

class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Tuckerstriker12@127.0.0.1:3306/e_commerce_db'
    DEBUG = True