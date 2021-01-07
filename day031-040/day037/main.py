import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USRENAME = os.getenv("PIXELA_USRENAME")
PIXELA_USERS_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPHS_ENDPOINT = f"{PIXELA_USERS_ENDPOINT}/{PIXELA_USRENAME}/graphs"
GRAPHID = "graph1"
PIXELA_GRAPHID_ENDPOINT = f"{PIXELA_GRAPHS_ENDPOINT}/{GRAPHID}"


def create_user_account():
    json = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USRENAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=PIXELA_USERS_ENDPOINT, json=json)
    response.raise_for_status()
    print(response.text)


def create_graph():
    json = {
        "id": GRAPHID,
        "name": "Cycle Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    response = requests.post(url=PIXELA_GRAPHS_ENDPOINT,
                             json=json, headers=headers)
    response.raise_for_status()


def add_pixel(quantity: float):
    json = {
        "date": datetime.now().strftime("%Y%m%d"),
        "quantity": str(quantity)
    }

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    response = requests.post(url=PIXELA_GRAPHID_ENDPOINT,
                             json=json, headers=headers)
    response.raise_for_status()


def update_pixel(quantity: float):
    json = {
        "quantity": str(quantity)
    }

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    response = requests.put(url=f"{PIXELA_GRAPHID_ENDPOINT}/{datetime.now().strftime('%Y%m%d')}",
                            json=json, headers=headers)
    response.raise_for_status()


def delete_pixel():
    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    response = requests.delete(
        url=f"{PIXELA_GRAPHID_ENDPOINT}/{datetime.now().strftime('%Y%m%d')}", headers=headers)
    response.raise_for_status()
