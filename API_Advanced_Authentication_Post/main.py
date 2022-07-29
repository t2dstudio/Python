#..........POST..............
#uSING pIXELA API
import requests
from datetime import datetime


USERNAME = "t2dstudio"
TOKEN = "ijustcreatedthistoken"
GRAPH_ID = "graph1"

pixela_endpoint= "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = str(datetime.today().strftime("%Y%m%d"))
pixel_config = {
    "date": today,
    "quantity": input("How many kilometers did you cycle today?")
}
response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220728"
new_pixel_data = {
    "quantity": "6.8"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220728"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)