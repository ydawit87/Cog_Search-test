import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    COSMOS_DB_ENDPOINT = os.environ.get('COSMOS_DB_ENDPOINT')
    COSMOS_DB_KEY = os.environ.get('COSMOS_DB_KEY')
    COSMOS_DB_DATABASE_NAME = os.environ.get('COSMOS_DB_DATABASE_NAME')
    COSMOS_DB_CONTAINER_NAME = os.environ.get('COSMOS_DB_CONTAINER_NAME')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
