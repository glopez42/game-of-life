from abc import ABC, abstractmethod
from typing import Tuple
from typing import List

class Selection(ABC):

    @abstractmethod
    def makeSelection(self, population):
        pass

class SelectBest20(Selection):

    def makeSelection(self, population: List[Tuple]):
        sorted_by_fitness = sorted(population, key=lambda tup: tup[1], reverse=True)
        best20 = sorted_by_fitness[0:20]
        best = []
        bestFitness = best20[0][1]
        print("Best fitness: ", bestFitness)
        # removes the fitness value of each rule as it is not longer required
        for tuple in best20:
            best.append(tuple[0])
        return best, bestFitness