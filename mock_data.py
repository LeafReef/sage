import time
import requests
import random

URL = "http://localhost:3000/api/insert"

while True:
    sensor_data = {
        "temperature": random.randint(20, 25),
        "humidity": random.randint(30, 50)
    }

    # Send POST request
    response = requests.post(URL, data=sensor_data)
    print(response.text)

    # Delay for 1 sec
    time.sleep(1)
