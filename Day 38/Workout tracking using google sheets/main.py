import os
import requests
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = os.environ["SHEETY_URL"]

GENDER = "male"
WEIGHT = 75
HEIGHT = 175
AGE = 24

query_text = input("What have you done today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_config = {
    "query": query_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=URL, json=exercise_config, headers=headers)
data = response.json()
# print(data)

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
token = os.environ["token"]

basic_auth = {
    "Authorization": token
}

for exercise in data["exercises"]:
    sheet_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_URL, json=sheet_input, headers=basic_auth)
    print(sheet_response.text)
