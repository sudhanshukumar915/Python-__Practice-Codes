"""voice_assistant/
│── main.py
│── config.py
│── stt.py
│── tts.py
│── intents.py
│── actions.py
│── utils.py
│── logs/
│    └── assistant.log
│── data/
     └── notes.txt"""
#1st part
import os

# Vosk model path (download separately)
MODEL_PATH = "vosk-model-small-multilang"

# Logging path
LOG_FILE = os.path.join("logs", "assistant.log")

# Audio settings
SAMPLE_RATE = 16000
BLOCK_SIZE = 8000

# Default note file
NOTES_FILE = os.path.join("data", "notes.txt")

#2nd part
import pyttsx3
import logging

tts_engine = pyttsx3.init()

def speak(text: str):
    """Text-to-Speech with logging"""
    try:
        logging.info(f"TTS Speak: {text}")
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        logging.error(f"TTS Error: {e}")
        print("TTS error:", e)

#3rd part
import queue, sys, os, json, logging, time
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from config import MODEL_PATH, SAMPLE_RATE, BLOCK_SIZE

# Load Vosk model
if not os.path.isdir(MODEL_PATH):
    print("❌ Please download a Vosk model and set MODEL_PATH in config.py")
    sys.exit(1)

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, SAMPLE_RATE)
rec.SetWords(True)

audio_q = queue.Queue()

def audio_callback(indata, frames, time_info, status):
    if status:
        logging.warning(f"Audio status: {status}")
    audio_q.put(bytes(indata))

def listen_once(seconds=5) -> str:
    """Listen fixed time, return transcription text."""
    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE, dtype='int16',
                           channels=1, callback=audio_callback):
        start = time.time()
        rec.Reset()
        while time.time() - start < seconds:
            data = audio_q.get()
            rec.AcceptWaveform(data)

        res = rec.FinalResult()
        try:
            text = json.loads(res).get("text", "").strip()
        except:
            text = ""
        logging.info(f"STT Heard: {text}")
        return text

#4th part

import re

def parse_intent(text: str):
    """Very simple intent parsing with regex and keywords"""
    t = text.lower()

    if any(k in t for k in ["chrome kholo","chrome open","browser kholo"]):
        return ("open_app", {"app":"chrome"})
    if any(k in t for k in ["notepad","editor kholo"]):
        return ("open_app", {"app":"notepad"})
    if "youtube" in t:
        return ("open_url", {"url":"https://youtube.com"})
    if "time" in t or "samay" in t:
        return ("time_now", {})
    m = re.search(r"(search|dhundo|google pe|web search)\s+(.*)", t)
    if m:
        return ("web_search", {"q": m.group(2)})
    m = re.search(r"(note\s*(likho|banao)|yaad\s*rakhna)\s*(.*)", t)
    if m:
        return ("make_note", {"content": m.group(3)})
    m = re.search(r"(file\s*banao|naya\s*file)\s*([a-zA-Z0-9_\-\.]+)\s*(.*)", t)
    if m:
        return ("make_file", {"name": m.group(2), "content": m.group(3)})
    return ("unknown", {"text": t})

#5th part

import re

def parse_intent(text: str):
    """Very simple intent parsing with regex and keywords"""
    t = text.lower()

    if any(k in t for k in ["chrome kholo","chrome open","browser kholo"]):
        return ("open_app", {"app":"chrome"})
    if any(k in t for k in ["notepad","editor kholo"]):
        return ("open_app", {"app":"notepad"})
    if "youtube" in t:
        return ("open_url", {"url":"https://youtube.com"})
    if "time" in t or "samay" in t:
        return ("time_now", {})
    m = re.search(r"(search|dhundo|google pe|web search)\s+(.*)", t)
    if m:
        return ("web_search", {"q": m.group(2)})
    m = re.search(r"(note\s*(likho|banao)|yaad\s*rakhna)\s*(.*)", t)
    if m:
        return ("make_note", {"content": m.group(3)})
    m = re.search(r"(file\s*banao|naya\s*file)\s*([a-zA-Z0-9_\-\.]+)\s*(.*)", t)
    if m:
        return ("make_file", {"name": m.group(2), "content": m.group(3)})
    return ("unknown", {"text": t})

#6th part
import os, sys, subprocess, time, webbrowser, logging
from config import NOTES_FILE
from tts import speak

def do_action(intent, slots):
    try:
        if intent == "open_app":
            app = slots.get("app")
            if app == "chrome":
                possible = [
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                ]
                for p in possible:
                    if os.path.exists(p):
                        subprocess.Popen([p])
                        speak("Chrome khol diya.")
                        return
                speak("Chrome nahin mila, browser khol raha hoon.")
                webbrowser.open("https://google.com")
            elif app == "notepad":
                if sys.platform.startswith("win"):
                    subprocess.Popen(["notepad.exe"])
                    speak("Notepad khol diya.")
        elif intent == "open_url":
            webbrowser.open(slots["url"])
            speak("Website khol di.")
        elif intent == "time_now":
            now = time.strftime("%I:%M %p")
            speak(f"Abhi {now} baj rahe hain.")
        elif intent == "web_search":
            webbrowser.open(f"https://www.google.com/search?q={slots['q']}")
            speak(f"Google par search kiya: {slots['q']}")
        elif intent == "make_note":
            with open(NOTES_FILE, "a", encoding="utf-8") as f:
                f.write(slots["content"] + "\n")
            speak("Note save ho gaya.")
        elif intent == "make_file":
            with open(slots.get("name","new.txt"), "w", encoding="utf-8") as f:
                f.write(slots.get("content",""))
            speak("File bana di.")
        else:
            speak("Samajh nahi aaya. Dubara boliye.")
    except Exception as e:
        logging.error(f"Action Error: {e}")
        speak("Kuch error aa gaya.")

#7th part
import logging
from stt import listen_once
from intents import parse_intent
from actions import do_action
from tts import speak

# Setup logging
logging.basicConfig(filename="logs/assistant.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    speak("Assistant ready hai.")
    print("Press Enter, bolo 3-5 sec… (Ctrl+C exit)")

    while True:
        try:
            input(">>> Enter dabayein aur boliye: ")
            text = listen_once(5)
            print("You said:", text)
            if not text:
                speak("Kuch sunai nahi diya.")
                continue
            intent, slots = parse_intent(text)
            do_action(intent, slots)
        except KeyboardInterrupt:
            speak("Band kar raha hoon. Alvida.")
            break
