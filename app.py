from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Live 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")

    if "sad" in msg:
        reply = "I'm here for you. Try talking to someone."
    elif "pain" in msg:
        reply = "It might be stress. Drink warm water and rest."
    else:
        reply = "Tell me more about how you're feeling."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
    
        return jsonify({"object": str(e)})


# ---------------- RUN ----------------
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
