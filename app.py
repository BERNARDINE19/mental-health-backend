from flask import Flask, request, jsonify
from flask_cors import CORS

# ✅ CREATE APP FIRST
app = Flask(__name__)

# ✅ THEN APPLY CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ TEST ROUTE
@app.route("/", methods=["GET"])
def home():
    return "Backend Live 🚀"

# ✅ CHAT API
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"reply": "Invalid request"}), 400

        user_msg = data["message"]

        # ✅ SIMPLE RESPONSE (FOR DEMO)
        return jsonify({
            "reply": f"Hello! You said: {user_msg}"
        })

    except Exception as e:
        return jsonify({"reply": str(e)}), 500

# ✅ IMPORTANT FOR LOCAL RUN (Render uses gunicorn)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
