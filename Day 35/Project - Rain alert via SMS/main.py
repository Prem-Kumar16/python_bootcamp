import requests
# import os
from twilio.rest import Client

api_key = "c0bd86ff836f69e40395764b639d718a"
account_sid = "ACdf48635eeac68c1d820bdd7b7c59c543"
auth_token = "b4fc12311e0e1293b822ce583524d47f"

parameters = {
    "lat": 27.236880,
    "lon": 78.652530,
    "appid": api_key
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

twelve_hr_data = weather_data["list"][0:4]
# print(twelve_hr_data)

weather_codes = [data["weather"][0]["id"] for data in twelve_hr_data]
print(weather_codes)

for code in weather_codes:
    if code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today, so please remember to bring an ☂ ",
        from_="+19288778722",
        to="+91 99447 38905"
    )
    print(message.status)

# print(weather_data["list"][0]["weather"][0]["id"])
