

# 🤖 JARVIS — AI Voice Assistant

JARVIS is a powerful AI-powered voice assistant built using Python that automates daily activities through voice commands. It can call contacts, send messages, open applications, control system operations, and provide intelligent conversational responses using the Google Gemini API.

---

## 🚀 Features

🎙️ Speech Recognition (Voice Commands)  
🔊 Text-to-Speech Responses  
📞 Call Automation  
💬 Send Messages & WhatsApp Integration  
🖥️ Open & Control Applications  
🌐 Web Search & YouTube Automation  
🧠 Google Gemini AI Integration  
👁️ Face Authentication Security  
⚡ Real-Time Task Automation  
🗄️ SQLite Database Support  

---

## 🧠 Tech Stack

- Python  
- SpeechRecognition  
- pyttsx3  
- OpenCV (Face Recognition)  
- pvporcupine (Wake Word Detection)  
- Google Gemini API  
- PyAutoGUI  
- pywhatkit  
- Eel (Frontend UI Integration)  
- SQLite  

---

## 📂 Project Structure


voice-assistant/
│
├── engine/
│   ├── auth/                 # Face authentication
│   ├── command/              # Command handling logic
│   ├── features.py           # Assistant features
│   ├── helper.py             # Utility functions
│   └── config.py             # Configuration settings
│
├── run.py                    # Starts JARVIS
├── main.py                   # Core execution file
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Ismail-shaik786/voice-assistant.git
cd voice-assistant
````

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your Gemini API Key

Update your configuration file with:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run JARVIS

```bash
python run.py
```

---

## 🗣 Example Commands

* “Jarvis, open Chrome”
* “Jarvis, send WhatsApp message”
* “Jarvis, search YouTube for cybersecurity tutorials”
* “Jarvis, what is today’s news?”
* “Jarvis, call Alex”

---

## 🔐 Security

JARVIS includes face authentication before granting access, ensuring only authorized users can operate the assistant.

---

## 📌 Future Improvements

* Upgrade to latest Google GenAI SDK
* Add NLP intent classification
* Add GUI dashboard
* Add cloud deployment option

---

## 👨‍💻 Author

**Ismail Shaik**
Cybersecurity & AI Developer

---

⭐ If you like this project, consider giving it a star!

```

---


```
