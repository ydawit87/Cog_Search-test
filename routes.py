from flask import render_template, request
from app import app, cosmos_service, openai_service
import uuid
import datetime

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user-input']
        if openai_service is not None:
            ai_response = openai_service.generate_message(user_input)
        else:
            ai_response = 'OpenAI service not initialized.'
        if cosmos_service is not None:
            document = {
                'user-id': '1', # TODO: replace with 'user-id
                'conversation-id': str(uuid.uuid4()),
                'timestamp': datetime.datetime.now().isoformat(),
                'user_input': user_input,
                'ai_response': ai_response
            }
            cosmos_service.add_item(document)
        return render_template('chat.html', user_input=user_input, ai_response=ai_response)

    return render_template('chat.html')
