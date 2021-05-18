import Adafruit_DHT
import time 
import requests

URL = "https://leafreef.herokuapp.com/api/insert"
SECONDS = 5

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    # Read DHT data
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    # If both values are defined
    if humidity is not None and temperature is not None:
        # Format sensor data to JSON
        sensor_data = {
            "temperature": temperature,
            "humidity": humidity
        }

        # Send POST request to API
        response = requests.post(URL, data=sensor_data)
        print(response.text)

        time.sleep(SECONDS)
    # Failed to read sensor value, tries again
    else:
        print("Sensor failed")
        pass
