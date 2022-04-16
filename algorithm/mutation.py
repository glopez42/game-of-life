from abc import ABC, abstractmethod
from rule import Rule
import random

class Mutation(ABC):

    @abstractmethod
    def performMutation(self):
        pass


class HammingDistanceMutation(Mutation):

    # performs the correspondant mutations in each rule
    def performMutation(self, rule1: Rule, rule2: Rule):
        bitArray1 = rule1.getRuleList()
        bitArray2 = rule2.getRuleList()

        distance = self._getHammingDistance(bitArray1, bitArray2)
        numberOfMutations = 1 if distance >= 5 else 5

        for _ in range(numberOfMutations):
            bitArray1 = self.mutate(bitArray1)
            bitArray2 = self.mutate(bitArray2)

        rule1.setRule(bitArray1)
        rule2.setRule(bitArray2)

        return rule1, rule2

    # Returns the hamming distance between 2 arrays, works like a XOR gate
    def _getHammingDistance(self, array1, array2):
        distance = 0
        for bit1,bit2 in zip(array1, array2):
            if bit1 != bit2:
                distance += 1
        return distance

    # Takes a random position of the array and reverse its state
    def mutate(self, bitArray):
        length = len(bitArray)
        randomPos = random.randint(0, length - 1)
        previousState = bitArray[randomPos]
        bitArray[randomPos] = 0 if previousState == 1 else 1
        return bitArray