import random
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Predefined chatbot responses (mock)
responses = [
    "I'm here to help! How are you feeling today?",
    "That sounds tough. Do you want to talk about it?",
    "It's okay to feel this way. You're not alone.",
    "Can I suggest some relaxation exercises?",
    "Take a deep breath. I'm here to listen.",
    "Remember, you're stronger than you think!"
]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json  # Get user message
    user_message = data.get("message", "")  # Safely get message from JSON

    # Select a random response from the list
    ai_response = random.choice(responses)

    return jsonify({"response": ai_response})  # Return AI's response to frontend

if __name__ == '__main__':
    app.run(debug=True)
