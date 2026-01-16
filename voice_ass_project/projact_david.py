# requirements (install):
# pip install vosk pyttsx3 sounddevice simpleaudio

import queue, sys, os, json, re, webbrowser, time, subprocess
import sounddevice as sd
import pyttsx3
from vosk import Model, KaldiRecognizer

# --------- TTS ----------
tts = pyttsx3.init()
def speak(text):
    try:
        tts.say(text)
        tts.runAndWait()
    except Exception as e:
        print("TTS error:", e)

# --------- STT (Vosk) ----------
# Download a small Hindi/English model e.g. "vosk-model-small-hi" or "vosk-model-small-en-in"
# and set the path below:
MODEL_PATH = "vosk-model-small-hi"   # change to your downloaded model folder

if not os.path.isdir(MODEL_PATH):
    print("Please download a Vosk model and set MODEL_PATH.")
    sys.exit(1)

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)
rec.SetWords(True)

audio_q = queue.Queue()

def audio_callback(indata, frames, time_info, status):
    if status:
        print(status, file=sys.stderr)
    audio_q.put(bytes(indata))

def listen_once(seconds=5):
    """Press-then-speak style: record few seconds and return text."""
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        start = time.time()
        rec.Reset()
        while time.time() - start < seconds:
            data = audio_q.get()
            if rec.AcceptWaveform(data):
                pass
        # Final result
        res = rec.FinalResult()
        try:
            text = json.loads(res).get("text","").strip()
        except:
            text = ""
        return text

# --------- Intent parsing (very simple rules) ----------
def parse_intent(text):
    t = text.lower()

    # open app/browser
    if any(k in t for k in ["chrome kholo","chrome khol","chrome open","browser kholo"]):
        return ("open_app", {"app":"chrome"})
    if any(k in t for k in ["notepad","editor kholo","text pad"]):
        return ("open_app", {"app":"notepad"})
    if any(k in t for k in ["youtube kholo","youtube open"]):
        return ("open_url", {"url":"https://www.youtube.com"})
    # time
    if any(k in t for k in ["time kya hai","samay","kitna baj","what time"]):
        return ("time_now", {})
    # web search
    m = re.search(r"(search|dhundo|google pe|web search)\s+(.*)", t)
    if m:
        query = m.group(2)
        return ("web_search", {"q": query})
    # note
    m = re.search(r"(note\s*(likho|banao)|yaad\s*rakhna)\s*(.*)", t)
    if m:
        content = m.group(3).strip()
        return ("make_note", {"content": content})
    # make file
    m = re.search(r"(file\s*banao|naya\s*file)\s*([a-zA-Z0-9_\-\.]+)\s*(.*)", t)
    if m:
        filename = m.group(2)
        content = m.group(3).strip()
        return ("make_file", {"name": filename, "content": content})

    # open folder or file
    m = re.search(r"(folder|directory)\s*(kholo|open)\s*(.*)", t)
    if m:
        path = m.group(3).strip().strip('"')
        return ("open_path", {"path": path})

    return ("unknown", {"text": t})

# --------- Actions ----------
def do_action(intent, slots):
    try:
        if intent == "open_app":
            app = slots.get("app")
            if app == "chrome":
                # Windows example paths; change per OS
                possible = [
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                ]
                for p in possible:
                    if os.path.exists(p):
                        subprocess.Popen([p])
                        speak("Chrome khol diya.")
                        return
                speak("Chrome nahin mila, default browser khol raha hoon.")
                webbrowser.open("https://google.com")
            elif app == "notepad":
                if sys.platform.startswith("win"):
                    subprocess.Popen(["notepad.exe"])
                    speak("Notepad khol diya.")
                else:
                    speak("Notepad Windows par hota hai. Aapka OS batayein.")
        elif intent == "open_url":
            webbrowser.open(slots["url"])
            speak("Website khol di.")
        elif intent == "time_now":
            now = time.strftime("%I:%M %p")
            speak(f"Abhi {now} baj rahe hain.")
        elif intent == "web_search":
            q = slots["q"]
            webbrowser.open(f"https://www.google.com/search?q={q}")
            speak(f"Google par search kiya: {q}")
        elif intent == "make_note":
            txt = slots["content"] or ""
            with open("notes.txt", "a", encoding="utf-8") as f:
                f.write(txt + "\n")
            speak("Note save ho gaya.")
        elif intent == "make_file":
            name = slots.get("name","new.txt")
            content = slots.get("content","")
            with open(name, "w", encoding="utf-8") as f:
                f.write(content)
            speak(f"File {name} bana di.")
        elif intent == "open_path":
            path = slots["path"] or "."
            if sys.platform.startswith("win"):
                os.startfile(path)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])
            speak("Path khol diya.")
        else:
            speak("Samajh nahin aaya. Dubara boliye ya simple shabdon mein kahiye.")
    except Exception as e:
        print("Action error:", e)
        speak("Kuch error aa gaya.")

# --------- Main loop (push-to-talk) ----------
print("Press Enter, bolo 3-5 seconds… phir result suno. (Ctrl+C to exit)")
speak("Voice assistant tayyar hai.")
while True:
    try:
        input(">>> Enter dabayein aur boliye: ")
        text = listen_once(seconds=5)
        print("You said:", text)
        if not text:
            speak("Kuch sunai nahin diya.")
            continue
        intent, slots = parse_intent(text)
        do_action(intent, slots)
    except KeyboardInterrupt:
        speak("Band kar raha hoon. Alvida.")
        break
