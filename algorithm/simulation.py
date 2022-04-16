from math import sqrt
from universe import nextState
import random
import timeit
import gc

# Creates a simulation of an universe, used  for testing rules
class Simulation():

    def __init__(self, iterations, width, height, ruleDictionary):
        # fitness parameters
        self.n1 = 0 # square growths
        self.n2 = 0 # square shrinks
        self.m1 = 0 # population growth
        self.m2 = 0 # population descreases
        self.actualPop = 0 # initial number of alive cells
        self.lastPop = 0 # number of alive cells in last iteration
        self.iter = iterations

        # central square parameters
        self.width =  width
        self.height = height
        self.center = [int(width/2) -1, int(height/2) -1]
        self.xLimits1 = self.center[0] - 20
        self.xLimits2 = self.center[0] + 20
        self.yLimits1 = self.center[1] - 20
        self.yLimits2 = self.center[1] + 20

        # first state of the universe
        self.universe = [[ 1  for i in range(width)] for j in range(height)]
        self._set_initial_state()
        self.rule = ruleDictionary
        self.aliveCells = []

    def runSimulation(self):
        for _ in range(self.iter):
            self.universe = nextState(self.rule, self.universe)
            self._check_limits()
            self._check_population()

        gc.collect()
        return self._return_parameters()

    def _return_parameters(self):
        c1 = self._calculate_c1()
        return {
            "N1" : self.n1,
            "N2" : self.n2,
            "L" : self.iter,
            "M1" : self.m1,
            "M2" : self.m2,
            "C1" : c1
        }
    
    def _calculate_c1(self):
        xSum = 0
        ySum = 0

        for cell in self.aliveCells:
            xSum += cell[0]
            ySum += cell[1]
        
        if self.aliveCells:
            # gravity center coordinates
            x = round(xSum / self.actualPop)
            y = round(ySum / self.actualPop)
        else:
            x = self.center[0]
            y = self.center[1]

        # center coordinates
        xCenter = self.center[0]
        yCenter = self.center[1]

        # euclidean distance between gravity center and universe center
        distance = sqrt((x - xCenter)**2 + (y - yCenter)**2)

        return 1 + (distance / self.width)
    
    def _check_population(self):
        # if there is a population decrease
        if self.lastPop > self.actualPop:
            self.m2 += 1
        # if there is a population growth
        elif self.lastPop < self.actualPop:
            self.m1 += 1
        self.lastPop = self.actualPop

    def _check_limits(self):
        outOfLimits = []
        insideLimits = []
        self.actualPop = 0

        # checks if the alive cells are out of the actual limits
        for y in range(self.height):
            for  x in range(self.width):
                state = self.universe[y][x]
                if state == 0:
                    self.actualPop += 1
                    if not self._inside_limits(x, y):
                        outOfLimits.append((x,y))
                    else:
                        insideLimits.append((x,y))
                      
        # if there are alive cells out of the limits
        if outOfLimits:
            self.aliveCells = outOfLimits
            self._grow_square(outOfLimits)
        else:
            self.aliveCells = insideLimits
            self._shrink_square(insideLimits)

    
    def  _grow_square(self, aliveCells):
        x1 = self.xLimits1 - 1
        x2 = self.xLimits2 + 1
        y1 = self.yLimits1 - 1
        y2 = self.yLimits2 + 1

        while not (self._inside_square(x1, x2, y1, y2, aliveCells)):
            x1 -= 1
            x2 += 1
            y1 -= 1
            y2 += 1
        
        # if there has been a growth
        if  x1 != self.xLimits1:
            self.xLimits1 = x1
            self.xLimits2 = x2
            self.yLimits1 = y1
            self.yLimits2 = y2
            self.n1 += 1
    
    def _shrink_square(self, aliveCells):
        x1 = self.xLimits1 + 1
        x2 = self.xLimits2 - 1
        y1 = self.yLimits1 + 1
        y2 = self.yLimits2 - 1

        while self._inside_square(x1, x2, y1, y2, aliveCells):
            x1 += 1
            x2 -= 1
            y1 += 1
            y2 -= 1
        
        # if there has been a decrease
        if  x1 != self.xLimits1:
            self.xLimits1 = x1
            self.xLimits2 = x2
            self.yLimits1 = y1
            self.yLimits2 = y2
            self.n2 += 1

    def _set_initial_state(self):
        for y in range(self.height):
            for x in range(self.width):
                # random state for the middle area
                if self._inside_limits(x,y):
                    # 25% chance of being alive
                    choice = random.choice([1,1,1,0])
                    self.universe[y][x] = choice
                    if choice == 0:
                        self.lastPop += 1
                else:
                    self.universe[y][x] = 1



    def _inside_limits(self, x, y):
        return x >= self.xLimits1 and x <= self.xLimits2 and y >= self.yLimits1 and y <= self.yLimits2
    
    def _inside_square(self, x1, x2, y1, y2, aliveCells):

        if x1 < 0 or y1 < 0 or x2 >= self.width or y2 >= self.height:
            return True
        
        if x1 >= x2 or y1 >= y2:
            return False
        
        inside = True
        for cell in aliveCells:
            x = cell[0]
            y = cell[1]

            if not (x >= x1 and x <= x2 and y >= y1 and y <= y2):
                inside = False
                break
        
        return inside
    