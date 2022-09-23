import requests
from datetime import datetime

USERNAME = "premk"
TOKEN = "your_token"

pixela_endpoint = "https://pixe.la/v1/users"

profile_page = "https://pixe.la/@premk"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"

graph_config = {
    "id": graph_id,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
today_in_str = today.strftime("%Y%m%d")

post_endpoint = f"{graph_endpoint}/{graph_id}"

post_config = {
    "date": today_in_str,
    "quantity": input("How many kms did you cycle today? value here")
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

update_endpoint = f"{post_endpoint}/{today_in_str}"

update_config = {
    "quantity": "How many kms did you cycle today? value here"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
