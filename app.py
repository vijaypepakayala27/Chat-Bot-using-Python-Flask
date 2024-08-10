from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send
import openai
import uuid
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Get the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    room = uuid.uuid4().hex  # Generate a unique room ID for each session
    return render_template('index.html', room=room)

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    #send(f'Chat ID {room}.', to=room)

@socketio.on('message')
def handle_message(data):
    msg = data['message']
    room = data['room']
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg}
        ]
    )
    send(response.choices[0].message.content, to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)  # No SSL context here
