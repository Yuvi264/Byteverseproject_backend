from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# AI Chatbot API URL
AI_API_URL = "https://your-ai-chatbot.com/chat"


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json  # Get user message
    user_message = data["message"]

    # Send request to AI chatbot
    response = requests.post(AI_API_URL, json={"message": user_message})

    return jsonify(response.json())  # Return AI's response to frontend


if __name__ == '__main__':
    app.run(debug=True)
