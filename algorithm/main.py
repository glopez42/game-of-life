from algorithm.crossover import *
from algorithm.mutation import *
from algorithm.fitness import * 
from algorithm.init import * 

class Algorithm():

    def __init__(self) -> None:
        self.iter = 50
        self.crossover = SinglePointCrossover()
        self.mutation = HammingDistanceMutation()
        self.population = []
        self.populationLength = 50

        
    def run(self):
        # sets up the population
        self._initPopulation()
        return


    def _initPopulation(self):
        # Initial rule from Bays space
        initialRule = getBaysSpaceRule()

        # First 10 rules without mutations
        for _ in range(10):
            self.population.append(initialRule)

        # Performs 10 single mutations
        for _ in range(10):
            mutatedRule = self.mutation.mutate(initialRule.getRuleList())
            self.population.append(mutatedRule)
        
        # Performs 10 double mutations
        for _ in range(10):
            mutatedRule = initialRule
            for _ in range(2):
                mutatedRule = self.mutation.mutate(mutatedRule.getRuleList())
            self.population.append(mutatedRule)
        
        # Performs 10 triple mutations
        for _ in range(10):
            mutatedRule = initialRule
            for _ in range(3):
                mutatedRule = self.mutation.mutate(mutatedRule.getRuleList())
            self.population.append(mutatedRule)
        
        # Performs 10 cuadruple mutations
        for _ in range(10):
            mutatedRule = initialRule
            for _ in range(4):
                mutatedRule = self.mutation.mutate(mutatedRule.getRuleList())
            self.population.append(mutatedRule)
