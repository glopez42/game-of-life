from abc import ABC, abstractmethod
from rule import Rule

class Crossover(ABC):

    @abstractmethod
    def performCrossover(self):
        pass


class SinglePointCrossover(Crossover):

    def performCrossover(self, rule1: Rule, rule2: Rule):
        bitArray1 = rule1.getRuleList()
        bitArray2 = rule2.getRuleList()

        length = len(bitArray1)

        newBitArray = bitArray1[0:length/2] + bitArray2[length/2:length]

        return Rule(newBitArray) 