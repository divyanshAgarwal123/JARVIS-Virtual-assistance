# 🤖 Jarvis - Virtual Assistant (Not AI)

A Python-based virtual assistant inspired by J.A.R.V.I.S from Iron Man. **This is not an AI model** but a chatbot that follows predefined commands.

---

## ✨ Features
✅ **Voice Command Recognition** – Uses speech-to-text to process your commands.
✅ **Open Websites and Applications** – Launch apps and browse the internet hands-free.
✅ **Search the Web** – Fetch instant information from Google.
✅ **Automate Daily Tasks** – Perform automated actions with a single voice command.
✅ **Text-to-Speech (TTS)** – Uses AI-generated voice responses.

---

## 🚀 Installation Guide
### **1️⃣ Clone the Repository**
```bash
 git clone https://github.com/yourusername/Jarvis-Virtual-Assistant.git
 cd Jarvis-Virtual-Assistant
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Assistant**
```bash
python Jarvis.py
```

---

## 🗣 How to Use
- **Wake Word:** "Jarvis"
- **Example Commands:**
  - "Jarvis, introduce yourself" → Jarvis will introduce itself.
  - "Jarvis, search Wikipedia for [topic]" → Fetches Wikipedia information.
  - "Jarvis, search for [query]" → Searches the web using PyWhatKit.
  - "Jarvis, open Google" → Opens Google in your default browser.
  - "Jarvis, shutdown" → Exits the assistant.
  - If an unrecognized command is given, Jarvis will say, "Sorry, I didn't understand that."

### **Command Flow:**
1. Say "Jarvis" to activate.
2. Speak your command (e.g., "search Wikipedia for Python").
3. Jarvis processes the command and provides a response.
4. If recognized, it performs the action; otherwise, it asks for clarification.

---

## 📌 Requirements
- Python 3.x
- `SpeechRecognition` (for voice input)
- `pyttsx3` (for text-to-speech)
- `wikipedia` (for fetching info)
- `pyaudio` (for microphone support)
- `pywhatkit` (for playing YouTube videos)
- `datetime` (for fetching time)

---

## 📜 License
This project is **open-source** and free to use under the MIT License.

---

## ⭐ Support & Contributions
Found a bug? Have a feature request? Feel free to **open an issue** or submit a **pull request**!

**Star ⭐ this repository to show support!** 🚀
