from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Live 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("message", "")

        if "sad" in msg.lower():
            reply = "I'm here for you. Try talking to someone."
        elif "pain" in msg.lower():
            reply = "It might be stress. Drink warm water and rest."
        else:
            reply = "Tell me more about how you're feeling."

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)})

if __name__ == "__main__":
    app.run()
