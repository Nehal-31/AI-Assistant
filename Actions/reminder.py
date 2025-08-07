from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from speech.speak import speak
import re

scheduler = BackgroundScheduler()
scheduler.start()

def parse_time(text):
   
    match = re.search(r"in (\d+) (second|seconds|minute|minutes|hour|hours)", text)
    if match:
        amount = int(match.group(1))
        unit = match.group(2)

        now = datetime.now()
        if "second" in unit:
            return now + timedelta(seconds=amount)
        elif "minute" in unit:
            return now + timedelta(minutes=amount)
        elif "hour" in unit:
            return now + timedelta(hours=amount)
    return None

def remind(message):
    speak(f"Reminder: {message}")

def set_reminder(text):
    time_obj = parse_time(text)
    if not time_obj:
        return "Sorry, I couldn't understand the reminder time."

    match_msg = re.search(r"remind me to (.+)", text)
    if match_msg:
        message = match_msg.group(1)
    else:
        message = "This is your reminder."


    scheduler.add_job(remind, 'date', run_date=time_obj, args=[message])
    return f"Okay, I will remind you to {message} at {time_obj.strftime('%I:%M %p')}."
