import time
import requests
import random

URL = "https://leafreef.herokuapp.com/api/insert"
SECONDS = 5

while True:
    sensor_data = {
        "temperature": random.randint(20, 25),
        "humidity": random.randint(40, 50)
    }

    response = requests.post(URL, data=sensor_data)
    print(response.text)

    time.sleep(SECONDS)
