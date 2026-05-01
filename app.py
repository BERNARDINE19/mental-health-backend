from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# 🔥 FIX CORS PROPERLY
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return "Backend Live 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")

    if "hello" in msg.lower():
        reply = "Hello! How can I help you?"
    else:
        reply = "Tell me more."

    return jsonify({"reply": reply})
