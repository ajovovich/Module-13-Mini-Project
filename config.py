import psycopg2

connection = psycopg2.connect(
    host="dpg-cud70nlumphs73dhp3q0-a:5432",
    database="e_commerce_api_mb3a",
    user="e_commerce_api_mb3a_user",
    password="3kb0SebgcnOi5zypkk4y1aD1Qx5gABT2"
)
   
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Tuckerstriker12@127.0.0.1:3306/e_commerce_db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True

class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Tuckerstriker12@127.0.0.1:3306/e_commerce_db'
    DEBUG = True