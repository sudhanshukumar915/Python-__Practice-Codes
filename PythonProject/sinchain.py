# sinchain.py - The Gemini Core Hybrid Intelligence

import time
import ollama
import speech_recognition as sr
import google.generativeai as genai

# Hamare banaye hue modules ko import karna
import config
from skills.basic_skills import open_notepad, play_on_youtube
from core_utils import speak, listen_for_command

# --- Gemini Connection Setup ---
gemini_model = None
try:
    if config.GEMINI_API_KEY and "यहाँ" not in config.GEMINI_API_KEY:
        genai.configure(api_key=config.GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel('gemini-1.5-pro-latest')
        print("Gemini Core connection successful.")
    else:
        print("WARNING: Gemini API Key not found. Running in offline-only mode.")
except Exception as e:
    print(f"WARNING: Could not connect to Gemini. Running in offline-only mode. Error: {e}")


def handle_command(command):
    """Faisla leta hai: Pehle local commands, phir default me Gemini, aur failure par local AI"""

    # --- STEP 1: Check for local system commands ---
    if ('ओपन' in command and 'नोटपैड' in command) or 'open notepad' in command:
        open_notepad()
        return True
    elif 'youtube par' in command or 'यूट्यूब पर' in command:
        play_on_youtube(command)
        return True
    elif any(ext in command for ext in ['baat karna band karo', 'exit', 'quit']):
        speak("ठीक है सुधांशु, अलविदा!")
        return False  # Main loop ko band karne ka signal

    # --- STEP 2: Default to Gemini (Cloud AI) ---
    if gemini_model:
        speak("ठीक है, मैं इस पर सोच रहा हूँ...")
        try:
            response = gemini_model.generate_content(command)
            speak(response.text)
            return True  # Kaam ho gaya
        except Exception as e:
            print(f"Gemini API Error: {e}. Falling back to local model.")
            speak("जेमिनी से कनेक्ट नहीं हो पा रहा हूँ। अपने लोकल दिमाग का इस्तेमाल कर रहा हूँ।")
            # Agar Gemini fail hota hai, to STEP 3 par jao

    # --- STEP 3: Fallback to Local AI (Ollama) ---
    # Yeh tabhi chalega agar Gemini model nahi hai ya fail ho gaya hai
    speak("अपने लोकल दिमाग से सोच रहा हूँ...")
    try:
        response = ollama.chat(
            model=config.MODEL_NAME,
            messages=[{'role': 'user', 'content': command}]
        )
        answer = response['message']['content']
        speak(answer)
    except Exception as e:
        print(f"Ollama model error: {e}")
        speak("माफ़ कीजिये, मेरा लोकल दिमाग भी काम नहीं कर रहा है।")

    return True


# ... baaki ka main_loop aur if __name__ == "__main__": wala code waisa hi rahega ...
def main_loop():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Microphone calibrated.")
        print(f"Wake word is: '{config.WAKE_WORD}'. Waiting...")
        while True:
            try:
                audio = r.listen(source, phrase_time_limit=4)
                text = r.recognize_google(audio, language='en-in')
                if config.WAKE_WORD.lower() in text.lower():
                    speak("जी?")
                    command = listen_for_command()
                    if command and command != "none":
                        if not handle_command(command):
                            break
                    print(f"\nWaiting for wake word '{config.WAKE_WORD}'...")
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                time.sleep(2)
            except Exception:
                pass


if __name__ == "__main__":
    try:
        ollama.list()  # Yeh check karne ke liye ki backup system online hai
        print("Ollama (Backup Brain) server confirmed.")
        speak("Sinchain Mark III... Gemini Core is online.")
        main_loop()
    except Exception as e:
        print(f"CRITICAL ERROR: Ollama server not found. Error: {e}")
        speak("Ollama सर्वर (मेरा बैकअप दिमाग) चालू नहीं है। कृपया पहले उसे चालू करें।")
