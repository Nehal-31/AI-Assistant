from actions.email import send_email
from actions.weather import get_weather
from actions.reminder import set_reminder
from actions.query import answer_query

def handle_intent(text):
    text = text.lower()
    
    if "email" in text:
        return send_email(text)
    elif "weather" in text:
        return get_weather(text)
    elif "reminder" in text:
        return set_reminder(text)
    elif "query" in text or "question" in text:
        return answer_query(text)
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"
    
