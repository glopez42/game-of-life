from abc import ABC, abstractmethod

class Fitness(ABC):

    @abstractmethod
    def fitnessFunction(self):
        pass
    