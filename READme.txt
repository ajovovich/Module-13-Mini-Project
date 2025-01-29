Advanced E-commerce API
This project implements an advanced e-commerce API using Python, Flask, and Flask-SQLAlchemy. It provides functionalities for customer management, product catalog browsing, order placement, and administrative tasks, all secured with JWT authentication.

Features

Customer Management:
Create, read, update, and delete customer profiles.
Manage customer accounts with secure password storage.


Product Catalog:
Add, retrieve, update, and delete products.
List all available products with details.


Order Processing:
Place new orders with selected products and customer information.
Retrieve order details by ID.


Administration:
JWT-based authentication with role-based authorization.
Customer and CustomerAccount endpoints accessible only by administrators.

Performance Optimization:
Flask-Caching for request caching.
Flask-Limiter for rate limiting (100 requests per day per endpoint).


Database Integration:
Utilizes MySQL database via Flask-SQLAlchemy.
Defines models for Customers, CustomerAccounts, Products, and Orders with relationships.