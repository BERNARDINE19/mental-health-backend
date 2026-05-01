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

    if not data or "message" not in data:
        return jsonify({"reply": "Invalid request"}), 400

    msg = data["message"]

    return jsonify({
        "reply": f"Hello! You said: {msg}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
