from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ===============================
# USER DATA (Temporary dictionary)
# ===============================
users = {}

# ===============================
# EMERGENCY KEYWORDS
# ===============================
EMERGENCY_KEYWORDS = [
    "chest pain", "difficulty breathing", "heart attack",
    "stroke", "seizure", "unconscious", "severe bleeding"
]

# ===============================
# MEDICAL CONTEXT
# ===============================
MEDICAL_CONTEXT = """
Use WHO and CDC style guidance.
Do NOT prescribe or diagnose.
Advise seeing a licensed doctor.
"""

# ===============================
# ROUTES
# ===============================
@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            return render_template("signup.html", error="Username already exists")
        users[username] = password
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=session["user"])

@app.route("/chatbot")
def chatbot():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("chatbot.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "").lower()

    # Emergency detection
    for k in EMERGENCY_KEYWORDS:
        if k in msg:
            return jsonify({
                "reply": "⚠️ This may be a medical emergency. Please contact emergency services immediately."
            })

    prompt = f"""
{MEDICAL_CONTEXT}

Rules:
- Do NOT prescribe medicines
- Do NOT diagnose
- Give general advice only
- Suggest seeing a doctor

User: {msg}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "Error connecting to medical assistant."})

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
