
import os

# These defaults work with the docker-compose file below
DB_HOST = os.environ.get('DB_HOST', 'db') 
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'rootpassword')
DB_NAME = os.environ.get('DB_NAME', 'student_db')
SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
