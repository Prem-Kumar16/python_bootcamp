import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 10.349821  # Your latitude
MY_LONG = 77.976194  # Your longitude

my_email = "premrajreddy26@gmail.com"
password = "mjtrnbiprsgkejxs"


def if_iss_is_above():
    responses = requests.get(url="http://api.open-notify.org/iss-now.json")
    responses.raise_for_status()
    datum = responses.json()

    iss_latitude = float(datum["iss_position"]["latitude"])
    iss_longitude = float(datum["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    minimum_lat = MY_LAT - 5
    maximum_lat = MY_LAT + 5

    minimum_lng = MY_LONG - 5
    maximum_lng = MY_LONG + 5

    if minimum_lat <= iss_latitude <= maximum_lat:
        if minimum_lng <= iss_longitude <= maximum_lng:
            return True
    else:
        return False


def if_its_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    if hour < sunrise or hour > sunset:
        return True
    else:
        return False


def email_me():
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="premrajreddy16@gmail.com",
                            msg=f"Subject:Hello from ISS\n\n"
                                f"Hi buddy,\n"
                                f"I have been wondering where you live and thank god I found you finally\n"
                                f"Please look up, I am waiting for you in the sky & I am so eager and I can't wait")


while True:
    time.sleep(60)
    # If the ISS is close to my current position
    if if_iss_is_above():
        # and it is currently dark
        if if_its_dark():
            # Then email me to tell me to look up.
            email_me()

    # BONUS: run the code every 60 seconds.
