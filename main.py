import Adafruit_DHT
from time import sleep
import requests

URL = "https://api-aura.herokuapp.com/api/set-sensor-value"

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

        print(sensor_data)

        # Send POST request
        # response = requests.post(URL, data=sensor_data)
        # print(response.text)

        # Pause for 1 second
        sleep(1)
    # Failed to read sensor value, tries again
    else:
        print("Sensor failed")
        pass
