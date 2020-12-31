import sys
import random
from dotenv import load_dotenv
import requests
from datetime import datetime, timezone
import os
import smtplib

DEBUG = True

load_dotenv()

BOT_EMAIL_ADDRESS = os.getenv("BOT_EMAIL_ADDRESS")
BOT_EMAIL_PASSWORD = os.getenv("BOT_EMAIL_PASSWORD")
MY_EMAIL_ADDRESS = os.getenv("MY_EMAIL_ADDRESS")

LOS_ANGELES_LAT = 34.052235
LOS_ANGELES_LONG = -118.243683

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
if DEBUG or (abs(iss_latitude - LOS_ANGELES_LAT) <= 5 and abs(iss_longitude - LOS_ANGELES_LONG) <= 5):
    parameters = {
        "lat": LOS_ANGELES_LAT,
        "lng": LOS_ANGELES_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = datetime.strptime(
        data["results"]["sunrise"], '%Y-%m-%dT%H:%M:%S+00:00')
    sunset = datetime.strptime(
        data["results"]["sunset"], '%Y-%m-%dT%H:%M:%S+00:00')

    time_now = datetime.utcnow()

    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
    if time_now.hour < sunrise.hour and time_now.hour > sunset.hour:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=BOT_EMAIL_ADDRESS,
                             password=BOT_EMAIL_PASSWORD)
            connection.sendmail(from_addr=BOT_EMAIL_ADDRESS, to_addrs=MY_EMAIL_ADDRESS,
                                msg=f"Subject:Look Up 👆\n\nThe ISS is above you in the sky.".encode("utf8"))
