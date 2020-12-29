##################### Extra Hard Starting Project ######################
import pandas
import sys
import os
from dotenv import load_dotenv
import datetime as dt
import random
import smtplib

load_dotenv()

DEBUG = True

BOT_EMAIL_ADDRESS = os.getenv("BOT_EMAIL_ADDRESS")
BOT_EMAIL_PASSWORD = os.getenv("BOT_EMAIL_PASSWORD")
MY_EMAIL_ADDRESS = os.getenv("MY_EMAIL_ADDRESS")


# 1. Update the birthdays.csv
birthdays = pandas.read_csv(os.path.join(sys.path[0], "birthdays.csv"))

if DEBUG:
    # delete all existing entries
    birthdays = birthdays[0:0]
    # add fake entry addressed to myself
    birthdays = birthdays.append({
        "name": "Junhong",
        "email": MY_EMAIL_ADDRESS,
        "year": 0,
        "month": 0,
        "day": 0,
    }, ignore_index=True)

birthdays = birthdays.to_dict(orient="records")

now = dt.datetime.now()

for birthday in birthdays:
    # 2. Check if today matches a birthday in the birthdays.csv
    if now.month == birthday['month'] and now.day == birthday['day']:
        is_today_birthday = True

    if DEBUG:
        is_today_birthday = True

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if not is_today_birthday:
        continue

    with open(os.path.join(sys.path[0], f"letter_templates/letter_{random.randint(1, 3)}.txt")) as file:
        letter_template = file.read()
    letter = letter_template.replace("[NAME]", birthday['name'])

    # 4. Send the letter generated in step 3 to that person's email address.
    message = f"From: {BOT_EMAIL_ADDRESS}\r\nTo: {birthday['email']}\r\nSubject: Happy Birthday\r\n\r\n{letter}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=BOT_EMAIL_ADDRESS,
                         password=BOT_EMAIL_PASSWORD)
        connection.sendmail(from_addr=BOT_EMAIL_ADDRESS, to_addrs=birthday['email'],
                            msg=message.encode("utf8"))
