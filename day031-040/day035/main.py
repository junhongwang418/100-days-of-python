from dotenv import load_dotenv
import requests
import os
from twilio.rest import Client

load_dotenv()


OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

LOS_ANGELES_LAT = 34.052235
LOS_ANGELES_LONG = -118.243683

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

params = {
    "lat": LOS_ANGELES_LAT,
    "lon": LOS_ANGELES_LONG,
    "appid": OPEN_WEATHER_MAP_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()

weather_data = response.json()

hourly = weather_data.get("hourly")[:12]

for data in hourly:
    if data.get("weather")[0].get("id") < 700:
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(message.status)
        break
