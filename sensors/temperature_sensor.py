from .sensor import Sensor
from random import random

class TemperatureSensor(Sensor):
    
    def _get_value(self) -> float:
        return random()
