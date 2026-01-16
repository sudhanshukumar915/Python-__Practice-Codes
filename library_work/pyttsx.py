import pyttsx3

# Engine initialize करो
engine = pyttsx3.init()

# Default text बोलवाओ
engine.say("Hello ! how are you !")
engine.runAndWait()

# Rate और volume check और set करो
rate = engine.getProperty('rate')
print(f"Default Rate: {rate}")
engine.setProperty('rate', 100) # 100 words per minute

volume = engine.getProperty('volume')
print(f"Default Volume: {volume}")
engine.setProperty('volume', 1.0) # Max volume

# Custom text बोलवाओ
engine.say("Now speaking with custom speed and volume.")
engine.runAndWait()
