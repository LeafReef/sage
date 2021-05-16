import requests

URL = "http://localhost:3000/api/insert"

sensor_data = {"temperature": 5, "humidity": 5}

response = requests.post(URL, data=sensor_data)
print(response.text)
