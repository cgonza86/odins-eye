from abc import ABC, abstractmethod
from statistics import mean

class Sensor(ABC):
    def __init__(
            self, 
            id: int, 
            threshold: float, 
            buffer_size: int = 10, 
            scale: float = 1
    ):
        self.__id = id
        self.__scale = scale
        self.__value = 0
        self.__buffer = [0] * buffer_size
        self.__changed = True
        self.__threshold = threshold
    
    @property
    def id(self) -> int:
        return self.__id
    
    def read(self) -> float:
        self.__changed = False
        return self.__value
    
    @property
    def has_changed(self) -> bool:
        return self.__changed
        
    def sample(self):
        actual_value = self._get_value()
        self.__buffer = [actual_value] + self.__buffer[0: -1]
        temp_value = mean(self.__buffer)
        if abs(self.__value - temp_value) >= (self.__value * self.__threshold):
            self.__changed = True
        self.__value = temp_value
           
    @abstractmethod
    def _get_value(self) -> float:
        pass
