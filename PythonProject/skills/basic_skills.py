# skills/basic_skills.py
import os
import pywhatkit
from core_utils import speak # Hum sinchain.py se speak function ko import kar rahe hain

def open_notepad():
    """Notepad kholta hai."""
    speak("ठीक है, नोटपैड खोल रहा हूँ।")
    os.system("start notepad")

def play_on_youtube(query):
    """YouTube par video chalata hai."""
    # Command se "youtube par" jaise shabdon ko hatana
    search_query = query.replace('youtube par', '').replace('chalao', '').replace('play', '').strip()
    if search_query:
        speak(f"{search_query} यूट्यूब पर चलाया जा रहा है।")
        pywhatkit.playonyt(search_query)
    else:
        speak("यूट्यूब पर क्या चलाना है, कृपया साफ़-साफ़ बताएं।")

# Aap yahaan aur bhi functions bana sakte hain