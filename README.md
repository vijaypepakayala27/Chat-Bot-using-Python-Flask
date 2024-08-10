
# Flask OpenAI Chat Application

This repository contains a simple Flask application that integrates with OpenAI's GPT model to create a chat application. The app uses Flask-SocketIO to manage real-time communications between users and the GPT-4 model.

## Features

- **Real-Time Chat:** Users can send messages and receive responses from OpenAI's GPT model in real-time.
- **Unique Room IDs:** Each session is assigned a unique room ID to keep chats separate.
- **Flask-SocketIO Integration:** Real-time communication is managed using Flask-SocketIO.
- **OpenAI Integration:** The app interacts with OpenAI's GPT-4 model to generate responses to user inputs.

## Setup

### Prerequisites

- Python 3.x
- Flask
- Flask-SocketIO
- OpenAI Python client
- Python-dotenv


### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/flask-openai-chat.git
    cd flask-openai-chat
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set your OpenAI API key:

    Replace `your_secret_key` in the code with your actual OpenAI API key.

4. Run the application:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000/` to start chatting.

## Usage

- Navigate to the homepage, and you will be assigned a unique chat room.
- Start sending messages, and the GPT-4 model will respond to your queries in real-time.

## Notes

- Make sure to handle your OpenAI API key securely.
- This application is meant for testing purposes and may require modifications for production use.
