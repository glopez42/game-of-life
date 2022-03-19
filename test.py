import universe
from data import *

matrix = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]

result = matrix
for i in range(3):
    result = universe.nextState(ruleDictionary, result)
    print(result)


