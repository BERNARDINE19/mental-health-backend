from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# 🔥 Allow all origins (important for Flutter Web)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route("/")
def home():
    return "Backend Live 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")

    return jsonify({
        "reply": f"Hello! You said: {msg}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
