import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import random
import sys

load_dotenv()

BOT_EMAIL_ADDRESS = os.getenv("BOT_EMAIL_ADDRESS")
BOT_EMAIL_PASSWORD = os.getenv("BOT_EMAIL_PASSWORD")
MY_EMAIL_ADDRESS = os.getenv("MY_EMAIL_ADDRESS")

now = dt.datetime.now()

TUESDAY = 1

if now.weekday() == TUESDAY:
    with open(os.path.join(sys.path[0], "quotes.txt")) as file:
        quotes = file.readlines()
    quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=BOT_EMAIL_ADDRESS, password=BOT_EMAIL_PASSWORD)
        connection.sendmail(from_addr=BOT_EMAIL_ADDRESS, to_addrs=MY_EMAIL_ADDRESS,
                            msg=f"Subject:Weekly Quote\n\n{quote}".encode("utf8"))
