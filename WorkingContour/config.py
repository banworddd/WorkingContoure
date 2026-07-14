import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = bool(os.environ.get('DEBUG'))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split()

PG_USER = os.environ.get('POSTGRES_USER')
PG_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
PG_PORT = os.environ.get('POSTGRES_PORT')
PG_HOST = os.environ.get('POSTGRES_HOST')
PG_NAME = os.environ.get('POSTGRES_DB')
