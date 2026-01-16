import pyttsx3    #For changing text into Audio
from pydub import AudioSegment
from pydub.generators import Sine      #for adding background music

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 130)
engine.setProperty("volume", 1.0)

text = """Everyday sun rise because sun show how sun rise because sun burn everyday.
If someone burn everyday they rise. Like sun everyday in this life there are two things present:
first, you feel and love your pain otherwise you can go to die. There is no life for weak men."""

engine.save_to_file(text, "voice.wav")
engine.runAndWait()

voice = AudioSegment.from_file("voice.wav")

bass = Sine(40).to_audio_segment(duration=len(voice)) - 20
pulse = Sine(120).to_audio_segment(duration=len(voice)).apply_gain(-25)

background = bass.overlay(pulse)

final = voice.overlay(background)

final.export("dark_voice_message.mp3", format="mp3")

print(" Audio ready: dark_voice_message.mp3")
