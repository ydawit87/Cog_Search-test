from flask import Flask, render_template, request, jsonify, session
from config import TOKEN_LIMIT, USER_COLOR, AI_COLOR, AZURE_COSMOS_URL, AZURE_COSMOS_KEY, AZURE_COSMOS_DB, QUESTREPSTORE_CONTAINER, RESTOREAPP_CONTAINER
from chat import count_tokens, generate_ai_response
from models import CosmosDbService
import openai
import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Load OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set up Azure Cosmos DB client
questrepstore_service = CosmosDbService(AZURE_COSMOS_URL, AZURE_COSMOS_KEY, AZURE_COSMOS_DB, QUESTREPSTORE_CONTAINER)
restoreapp_service = CosmosDbService(AZURE_COSMOS_URL, AZURE_COSMOS_KEY, AZURE_COSMOS_DB, RESTOREAPP_CONTAINER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get user's message from form data
    message = request.form.get('message')

    # Validate token count
    if count_tokens(message) > TOKEN_LIMIT:
        return jsonify({'error': 'Token limit exceeded'}), 400

    # Generate AI response
    response = generate_ai_response(message)

    # Store user's message in Azure Cosmos DB
    questrepstore_service.add_item({
        'datetime': datetime.datetime.now().isoformat(),
        'message': message,
        'user_id': session['user_id']
    })

    # Store AI's response in Azure Cosmos DB
    restoreapp_service.add_item({
        'datetime': datetime.datetime.now().isoformat(),
        'response': response,
        'user_id': session['user_id']
    })

    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)

