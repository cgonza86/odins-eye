from time import sleep
from sensors.temperature_sensor import TemperatureSensor

temp_sensor = TemperatureSensor(id=10, threshold=0.1)

while True:
    temp_sensor.sample()

    if temp_sensor.has_changed:
        print(f"temperature: {temp_sensor.read()}")
    
    sleep(0.1)
