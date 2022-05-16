from algorithm.crossover import *
from algorithm.mutation import *
from algorithm.fitness import * 
from algorithm.init import * 
from algorithm.selection import *
import copy
import timeit


class Algorithm():

    def __init__(self, initialRule) -> None:
        self.iter = 0
        self.crossover = SinglePointCrossover()
        self.mutation = HammingDistanceMutation()
        self.fitness = FirstAproachFitness()
        self.selection = SelectBest20()
        self.population = []
        self.initialRule = initialRule
  
    def run(self, iterations) -> Rule:

        self.iter = iterations
        # sets up the population
        self._initPopulation()

        for i in range(self.iter - 1):
            start = timeit.default_timer()
            print("##### Iter " + str(i) + " started #####\n")
            
            # fitness and selection
            print("Fitness started...")
            startAux = timeit.default_timer()
            fitnessResults = self.fitness.fitnessFunction(self.population)
            stopAux = timeit.default_timer()
            print("Fitness ended in  " + str(stopAux - startAux) + " s")

            print("Selection started...")
            startAux = timeit.default_timer()
            selectionResults, bestFitness = self.selection.makeSelection(fitnessResults)
            stopAux = timeit.default_timer()
            print("Selection ended in  " +  str(stopAux - startAux) + " s")

            # crossover
            print("Crossover started...")
            startAux = timeit.default_timer()
            shuffledList = copy.deepcopy(selectionResults)
            random.shuffle(shuffledList)
            crossoverResults = []
            for i in range(10):
                rule1 = shuffledList[i]
                rule2 = shuffledList[i + 10]
                result = self.crossover.performCrossover(rule1, rule2)
                crossoverResults.append(result)
            stopAux = timeit.default_timer()
            print("Crossover ended in  " +  str(stopAux - startAux) + " s")
            
            # mutation
            print("Mutation started...")
            startAux = timeit.default_timer()
            mutationResults = []
            for i in range(10):
                rule1 = shuffledList[i]
                rule2 = shuffledList[i + 10]
                result1, result2 = self.mutation.performMutation(rule1, rule2)
                mutationResults.append(result1)
                mutationResults.append(result2)
            stopAux = timeit.default_timer()
            print("Mutation ended in  " + str(stopAux - startAux) + " s")
            
            # new population
            self.population = []
            self.population += selectionResults
            self.population += crossoverResults
            self.population += mutationResults
        
            stop = timeit.default_timer()
            print("\t---> Finished iteration in " + str(stop - start) + " s")

            # if the fitness is already quite good
            if bestFitness >= 1.65:
                break

        # last fitness and selection
        print("\n#### Last Fitness ####")
        fitnessResults = self.fitness.fitnessFunction(self.population)
        selectionResults, bestFitness = self.selection.makeSelection(fitnessResults)         
        
        # retrieves the best rule
        return selectionResults[0], bestFitness


    def _initPopulation(self):
        # Initial rule from Bays space
        initialRule = getBaysSpaceRule(self.initialRule)

        # First 10 rules without mutations
        for _ in range(10):
            rule = copy.deepcopy(initialRule)
            self.population.append(rule)

        # Performs 10 single mutations
        for _ in range(10):
            bitArray = self.mutation.mutate(initialRule.getRuleList())
            mutatedRule = Rule(bitArray)            
            self.population.append(mutatedRule)
        
        # Performs 10 double mutations
        for _ in range(10):
            mutatedRule = initialRule
            for _ in range(2):
                bitArray = self.mutation.mutate(mutatedRule.getRuleList())
                mutatedRule = Rule(bitArray)
            self.population.append(mutatedRule)
        
        # Performs 10 triple mutations
        for _ in range(10):
            mutatedRule = initialRule
            for _ in range(3):
                bitArray = self.mutation.mutate(mutatedRule.getRuleList())
                mutatedRule = Rule(bitArray)
            self.population.append(mutatedRule)
        
        # Performs 10 cuadruple mutations
        for _ in range(10):
            mutatedRule = initialRule
            for _ in range(4):
                bitArray = self.mutation.mutate(mutatedRule.getRuleList())
                mutatedRule = Rule(bitArray)
            self.population.append(mutatedRule)
