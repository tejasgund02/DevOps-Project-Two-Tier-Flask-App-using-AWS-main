import os

DB_HOST = os.getenv("DB_HOST", "db")          # service name in docker-compose
DB_USER = os.getenv("DB_USER", "flask_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "flask_password")
DB_NAME = os.getenv("DB_NAME", "flask_db")

SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")