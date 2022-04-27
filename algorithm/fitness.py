from abc import ABC, abstractmethod
from typing import Dict, List
from algorithm.simulation import Simulation
from rule import Rule
import timeit

class Fitness(ABC):

    @abstractmethod
    def fitnessFunction(self, population):
        pass
    

class FirstAproachFitness(Fitness):

    def __init__(self):
        self.iters = 200
        self.width = 200
        self.height = 200

    # calculates fitness of each rule and returns a list containing all fitness results
    def fitnessFunction(self, population: List[Rule]):

        results = []
        x = 1
        for rule in population:
            # runs a simulation of an universe during 300 iterations with that rule

            print("\tSimulation {} out of 50 started...".format(x))
            start = timeit.default_timer()
            simulation = Simulation(self.iters, self.width, self.height, rule.getRule())
            parameters = simulation.runSimulation()
            stop = timeit.default_timer()
            print("\tSimulation ended in  " + str(stop - start) + " s")
            
            fitness = self._calculate_fitness(parameters)
            results.append((rule, fitness))
            
            x += 1

        return results
    
    def _calculate_fitness(self, parameters: Dict):
        n1 = parameters["N1"]
        n2 = parameters["N2"]
        m1 = parameters["M1"]
        m2 = parameters["M2"]
        L = parameters["L"]
        c1 = parameters["C1"] 

        S1 = (n1 - n2 +  L) / L
        S2 = (m1 - m2 + L) / L
        f = (S1 * S2) / c1

        return f

