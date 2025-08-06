import pyttsx3

''' Initialize the TTS engine'''
engine = pyttsx3.init()

# You can customize voice, rate, and volume here
engine.setProperty('rate', 170)  # Speed of speech (default is ~200)
engine.setProperty('volume', 1.0)  # Max volume is 1.0

# Optionally select a specific voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Choose a voice (0: male, 1: female typically)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
