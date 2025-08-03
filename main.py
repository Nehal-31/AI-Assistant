import time
from speech.recognize import listen_to_user
from speech.speak import speak
from nlp.intent_handler import handle_intent

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        try:
            user_input = listen_to_user()
            if not user_input:
                speak("I didn't catch that. Could you please repeat?")
                continue

            if "exit" in user_input.lower() or "quit" in user_input.lower():
                speak("Goodbye!")
                break

            response = handle_intent(user_input)
            speak(response)
        
        except KeyboardInterrupt:
            speak("Assistant terminated.")
            break
        except Exception as e:
            speak("Sorry, something went wrong.")
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
