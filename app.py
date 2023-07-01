from flask import Flask
from config import Config
from services import CosmosDbService, OpenAIService


app = Flask(__name__)
app.config.from_object(Config)

cosmos_service = None
if app.config.get('COSMOS_DB_ENDPOINT') and app.config.get('COSMOS_DB_KEY'):
    cosmos_service = CosmosDbService(app.config['COSMOS_DB_ENDPOINT'], app.config['COSMOS_DB_KEY'], app.config['COSMOS_DB_DATABASE_NAME'], app.config['COSMOS_DB_CONTAINER_NAME'])

openai_service = None
if app.config.get('OPENAI_API_KEY'):
    openai_service = OpenAIService(app.config['OPENAI_API_KEY'])

import routes
