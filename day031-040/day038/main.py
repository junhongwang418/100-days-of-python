from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

NUTITIONIX_APP_ID = os.getenv("NUTITIONIX_APP_ID")
NUTITIONIX_API_KEY = os.getenv("NUTITIONIX_API_KEY")
NUTITIONIX_BASE_URL = "https://trackapi.nutritionix.com"
NUTITIONIX_NATURAL_EXERCISE_URL = f"{NUTITIONIX_BASE_URL}/v2/natural/exercise"
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")


def get_exercise_data(q: str):
    headers = {
        "x-app-id": NUTITIONIX_APP_ID,
        "x-app-key": NUTITIONIX_API_KEY
    }

    json = {
        "query": q,
    }

    response = requests.post(NUTITIONIX_NATURAL_EXERCISE_URL,
                             json=json, headers=headers)
    response.raise_for_status()
    return response.json()


def add_rows(data):
    for exercise in data["exercises"]:
        json = {
            "workout": {
                "date": datetime.now().strftime("%m/%d/%Y"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        response = requests.post(
            SHEETY_ENDPOINT, json=json, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
        response.raise_for_status()


add_rows(get_exercise_data(input("What workout did you do today?")))
