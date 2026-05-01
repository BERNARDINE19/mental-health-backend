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

<<<<<<< HEAD
        # ✅ SIMPLE RESPONSE (FOR DEMO)
        return jsonify({
            "reply": f"Hello! You said: {user_msg}"
        })

    except Exception as e:
        return jsonify({"reply": str(e)}), 500
=======
        prompt = f"""
You are a smart, emotionally intelligent AI assistant for Indian users.

Rules:
- Reply in same language (Hindi / Hinglish / English)
- Sound like a real human (friendly tone)
- Give specific helpful answers (not generic)
- Keep response short (2–3 lines)
- If emotional → support + suggestion
- If question → clear answer

Conversation:
{memory}

Assistant:
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:8b-instruct-q4_K_M",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        result = response.json()
        ai_reply = result.get("response", "").strip()

        if not ai_reply:
            ai_reply = "Thoda aur batao… main sun raha hoon."

        conversation_history.append(f"Assistant: {ai_reply}")

        return jsonify({"reply": ai_reply})

    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({"reply": "Server error, please try again"})
    
# ---------------- VISION ----------------
@app.route("/vision", methods=["POST"])
def vision():
    global last_vision_time

    try:
        if time.time() - last_vision_time < 2:
            return jsonify({"object": "Please wait..."})

        last_vision_time = time.time()

        if "image" not in request.files:
            return jsonify({"object": "No image received"})

        file = request.files["image"]
        filepath = "temp.jpg"
        file.save(filepath)

        img = cv2.imread(filepath)

        if img is None:
            return jsonify({"object": "Image read failed"})

        img = cv2.resize(img, (320, 320))

        results = model.predict(img, imgsz=320, conf=0.4)

        detected = []

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]
                detected.append(label)

        os.remove(filepath)

        if not detected:
            return jsonify({"object": "Nothing detected"})

        return jsonify({"object": ", ".join(set(detected))})

    except Exception as e:
        print("VISION ERROR:", e)
        return jsonify({"object": str(e)})


# ---------------- RUN ----------------
import os
>>>>>>> 4339227 (fix backend crash)

# ✅ IMPORTANT FOR LOCAL RUN (Render uses gunicorn)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
