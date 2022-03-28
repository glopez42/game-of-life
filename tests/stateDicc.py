from contexts import CONTEXTS
from ruleGL import RULEGL

ruleDictionary = {}

# Un diccionario para comprobar el estado por cada contexto
for i in range(512):
    ruleDictionary.update({ CONTEXTS[i] : RULEGL[i]})

print(len(ruleDictionary))

list = [0,1,0,0,0,0,0,0,0]

print(ruleDictionary.get(tuple(list)))