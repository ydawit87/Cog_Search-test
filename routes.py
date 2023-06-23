from flask import request, render_template
from app import app
from services import CosmosDbService
import uuid

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')
        response = generate_response(message)  # This is a placeholder. You'll replace this with the actual function to generate a response using GPT-3.
        document = {
            'id': str(uuid.uuid4()),
            'message': message,
            'response': response
        }
        cosmos_service = CosmosDbService(Config.COSMOS_DB_ENDPOINT, Config.COSMOS_DB_KEY, Config.COSMOS_DB_DATABASE_NAME, Config.COSMOS_DB_CONTAINER_NAME)
        cosmos_service.add_item_async(document)
        return render_template('index.html', message=message, response=response)
    else:
        return render_template('index.html')
