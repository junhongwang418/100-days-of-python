# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from twilio.rest import Client

load_dotenv()

KIWI_API_KEY = os.getenv("KIWI_API_KEY")
SHEETY_FLIGHT_DEALS_ENDPOINT = os.getenv("SHEETY_FLIGHT_DEALS_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
KIWI_LOCATIONS_QUERY_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

response = requests.get(SHEETY_FLIGHT_DEALS_ENDPOINT,
                        auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
response.raise_for_status()

data = response.json()

prices = data["prices"]

for price in prices:
    # params = {
    #     "apikey": KIWI_API_KEY,
    #     "term": price["city"]
    # }
    # response = requests.get(KIWI_LOCATIONS_QUERY_ENDPOINT, params=params)
    # response.raise_for_status()
    # data = response.json()
    # locations = data["locations"]

    # json = {
    #     "price": {
    #         "iataCode": locations[0]["code"]
    #     }
    # }
    # response = requests.put(f"{SHEETY_FLIGHT_DEALS_ENDPOINT}/{price['id']}", json=json, auth=(
    #     SHEETY_USERNAME, SHEETY_PASSWORD))
    # response.raise_for_status()

    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    six_month_from_today = today + timedelta(days=180)

    params = {
        "apikey": KIWI_API_KEY,
        "fly_from": "LAX",
        "fly_to": price["iataCode"],
        "date_from": tomorrow.strftime("%d/%m/%Y"),
        "date_to": six_month_from_today.strftime("%d/%m/%Y"),
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "curr": "USD"
    }

    response = requests.get(KIWI_SEARCH_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    flight = data["data"][0]

    if price["lowestPrice"] > flight["price"]:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=f"Flight to {price['city']} only costs {flight['price']}!",
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
