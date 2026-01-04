🏥 Medical Chatbot Web Application

A web-based medical assistant built using Python (Flask) and OpenAI, designed to provide general medical guidance, emergency awareness, voice input support, and a secure user dashboard.

⚠️ Disclaimer: This application does not provide medical diagnosis or prescriptions. It is intended for educational and informational purposes only.

📌 Features

🔐 User Authentication (Signup & Login)

📊 User Dashboard

💬 AI-Powered Medical Chatbot

🚨 Emergency Keyword Detection

🎤 Voice Input (Speech-to-Text)

👤 User Profile Display

🔙 Back-to-Dashboard Navigation

🎨 Modern Responsive UI

🧠 WHO / CDC-style Medical Guidance

🏗️ Project Structure
medical-chatbot/
│
├── app.py
├── requirements.txt
├── .env
│
├── static/
│   └── style.css
│
└── templates/
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    └── chatbot.html

⚙️ Technologies Used
Layer	Technology
Backend	Python, Flask
Frontend	HTML, CSS, JavaScript
AI	OpenAI GPT
Speech	Web Speech API
Security	Flask Sessions
Environment	python-dotenv
🛠️ Installation & Setup (Windows)
1️⃣ Clone or Download Project
git clone https://github.com/your-repo/medical-chatbot.git
cd medical-chatbot

2️⃣ Ensure Python is Installed
py --version


✔️ Python 3.10+ recommended

3️⃣ Install Dependencies
py -m pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a file named .env in the project root:

OPENAI_API_KEY=your_openai_api_key_here

5️⃣ Run the Application
py app.py

6️⃣ Open in Browser
http://127.0.0.1:5000

🔐 Authentication Flow

Signup with username & password

Login securely

Access dashboard

Open chatbot

Logout when finished

🚨 Emergency Detection

The chatbot automatically detects emergency phrases such as:

Chest pain

Difficulty breathing

Heart attack

Stroke

Seizure

Severe bleeding

⚠️ When detected, users are advised to contact emergency services immediately.

🎤 Voice Input

Click the 🎤 microphone button

Speak your medical question

Speech converts automatically into text

Supported on Chromium-based browsers (Chrome, Edge)

🧠 Medical AI Rules

The assistant:

Does NOT diagnose diseases

Does NOT prescribe medication

Provides general health advice only

Encourages consulting licensed medical professionals

📈 Future Enhancements

SQLite / PostgreSQL database

Password hashing (bcrypt)

Doctor appointment booking

Medical history tracking

Multilingual support

Admin dashboard

🧪 Tested Environment

OS: Windows 10 / 11

Python: 3.12

Browser: Chrome / Edge

📜 License

This project is released under the MIT License.

👨‍💻 Author

Developed for educational and academic purposes.