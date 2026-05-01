from flask import Flask, request, jsonify
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "*"}})

app = Flask(__name__)

# 🔥 FIX CORS (IMPORTANT)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return "Backend Live 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"reply": "No data received"})

        msg = data.get("message", "")

        print("MESSAGE RECEIVED:", msg)  # debug log

        if "hello" in msg.lower():
            reply = "Hello! How can I help you?"
        elif "sad" in msg.lower():
            reply = "I'm here for you. Try talking to someone."
        elif "pain" in msg.lower():
            reply = "It might be stress. Drink warm water and rest."
        else:
            reply = "Tell me more."

        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": str(e)})

# 🔥 IMPORTANT FOR RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
