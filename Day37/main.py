import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = "MY TOKEN"
USERNAME = "MY USERNAME"
GRAPH_ID = "MY GRAPH ID"

user_params = {
   "token": TOKEN,
   "username": USERNAME,
   "agreeTermsofService": "yes",
   "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
   "id": GRAPH_ID,
   "name": "Coding Graph",
   "unit": "hour",
   "type": "float",
   "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#CREATES A GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#print(today)

pixel_config = {
   "date": today.strftime("%Y%m%d"),
   "quantity": "4",
}

#CREATES A PIXEL IN GRAPH
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

#TO UPDATE A PIXEL on a SPECIFIC DATE

#today = datetime(year=2022, month=9, day=7)
#date = today.strftime("%Y%m%d")

#date_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

date_config = {
   "quantity": "2",
}

# response = requests.put(url=date_endpoint, json=date_config, headers=headers)
# print(response.text)

#DELETE A PIXEL on a SPECIFIC DATE

#delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

