# core_utils.py

import speech_recognition as sr
import pyttsx3

# --- Sinchain की आवाज़ और शुरुआती सेटअप ---
try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
except Exception as e:
    print(f"Error initializing TTS engine: {e}")

def speak(audio):
    """Sinchain का जवाब बोलकर सुनाता है"""
    print(f"Sinchain: {audio}")
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speaking: {e}")

def listen_for_command():
    """Microphone से user की आवाज़ सुनता है और टेक्स्ट में बदलता है"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for your command...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing command...")
        query = r.recognize_google(audio, language='hi-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        return "none" # Agar samajh na aaye
    except sr.RequestError:
        speak("माफ़ कीजिये, इंटरनेट शायद काम नहीं कर रहा है।")
        return "none"
    except Exception as e:
        print(f"Error during command recognition: {e}")
        return "none"