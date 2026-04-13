# =================================
# Mental Health Companion Backend
# =================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import cv2
import time
from ultralytics import YOLO

app = Flask(__name__)
CORS(app)

conversation_history = []
last_vision_time = 0

# Load YOLO
model = YOLO("yolov8n.pt")


# ---------------- HOME ----------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend Running"})


# ---------------- CHAT ----------------
@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history

    try:
        data = request.get_json()
        user_msg = data.get("message", "")

        conversation_history.append(f"User: {user_msg}")
        conversation_history = conversation_history[-8:]

        memory = "\n".join(conversation_history)

        prompt = f"""
You are a highly intelligent, emotionally aware AI assistant for Indian users.

GOAL:
- Give the BEST possible helpful answer every time
- Sound like a real human (not robotic)

RULES:
- Reply in same language (Hindi / Hinglish / English)
- Be natural, friendly, and smart
- Give specific answers (not generic)
- If emotional → support + 1 practical step
- If question → clear direct answer
- If song request → suggest 2–3 BEST songs only
- NEVER say "I am an AI"
- NEVER give vague replies like "tell me more"

STYLE:
- Short (2–3 lines)
- Real human tone

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
            timeout=40
        )

        result = response.json()
        ai_reply = result.get("response", "").strip()

        if not ai_reply:
            ai_reply = "thoda aur batao…"

        # ✅ FIXED LINE
        conversation_history.append(f"Assistant: {ai_reply}")

        return jsonify({"reply": ai_reply})

    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({"reply": str(e)})
    
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)