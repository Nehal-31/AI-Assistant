import smtplib
import ssl
from speech.speak import speak
from speech.recognize import listen_to_user
import os
from dotenv import load_dotenv

load_dotenv()  # Load email credentials from .env file

EMAIL_ADDRESS = os.getenv("risshikundu.83@gmail.com")
EMAIL_PASSWORD = os.getenv("Rishikundu27*")

def send_email():
    try:
        speak("Who is the recipient?")
        recipient = listen_to_user().replace(" ", "").lower()

        speak("What is the subject?")
        subject = listen_to_user()

        speak("What should I say in the message?")
        message = listen_to_user()

        full_email = f"Subject: {subject}\n\n{message}"

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, f"{recipient}@gmail.com", full_email)

        return f"Email sent to {recipient}."
    
    except Exception as e:
        print(f"[ERROR] {e}")
        return "Sorry, I couldn't send the email."
