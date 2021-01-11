import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_CUSTOMER_ACQUISITION_ENDPOINT = os.getenv(
    "SHEETY_CUSTOMER_ACQUISITION_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

print("Welcome to Junhong's Flight Club")
print("We find the best flight deals and email you.")
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
email = input("What is your email? ")

json = {
    "customer": {
        "firstName": firstname,
        "lastName": lastname,
        "email": email
    }
}
response = requests.post(SHEETY_CUSTOMER_ACQUISITION_ENDPOINT, json=json,
                         auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
response.raise_for_status()
print(response.text)
