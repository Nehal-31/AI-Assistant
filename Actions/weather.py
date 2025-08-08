import requests
import os
from dotenv import load_dotenv
from speech.speak import speak
from speech.recognize import listen_to_user

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather():
    try:
        speak("Please tell me the city name.")
        city = listen_to_user().strip()

        if not city:
            return "I didn't catch the city name."

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return f"Sorry, I couldn't find weather data for {city}."

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        weather_report = (f"The current temperature in {city} is {temp}°C with {description}. "
                          f"Humidity is {humidity}% and wind speed is {wind} meters per second.")

        return weather_report

    except Exception as e:
        print(f"[ERROR] {e}")
        return "Something went wrong while fetching the weather data."
