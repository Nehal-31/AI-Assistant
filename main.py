import time
from speech.recognize import listen_to_user
from speech.speak import speak
from nlp.intenthandler import handle_intent
def main():
    speak("Hello, I am your personal assistant. How can I help you today?")
    while True:
        user_input = listen_to_user()
        if user_input:
            response = handle_intent(user_input)
            speak(response)
        time.sleep(1)  # Adding a delay to avoid rapid looping 