from algorithm.main import Algorithm
from algorithm import init
from data import dbManager
from rule import Rule
import sys

if len(sys.argv) != 4:
    print("ERROR: start.py usage: \n\npython start.py [initial_rule] [result_name] [iterations]")
    exit(-1)

iter = int(sys.argv[3])
initialRuleName = sys.argv[1]
splitRule = initialRuleName.split("/")

Eb = int(splitRule[0][0])
Eh = int(splitRule[0][1])
Fb = int(splitRule[1][0])
Fh = int(splitRule[1][1])
initialRule = (Eb, Eh, Fb, Fh)

# Algorithm
rule, fitness = Algorithm(initialRule).run(iter)
dbManager.insertRule(sys.argv[2], rule.getRuleList())

# Mutations
rule2 = dbManager.getRuleByName(initialRuleName)
cont = 0
for bit1, bit2 in zip(rule.getRuleList(), rule2):
    if bit1 != bit2:
        print("Mutación en bit: ", cont)
    cont += 1



# Bays space: 35/33
# Interesantes: prueba, prueb2, prueba42
# Borrar: prueba2, prueba3, prueba8

# Bays space: 12/33
# Interesantes: prueba5 (Gliders), prueba6 (Gliders)
# Borrar: prueba4, prueba7

# Bays space: 23/44
# Interesantes: prueba9
# Borrar: 

# Bays space: 33/44 - Esta solo genera unos pocos patrones estáticos
# Interesantes: 
# Borrar: 

# Bays space: 24/44
# Interesantes: 
# Borrar: 

# Bays space caóticas: 14/33, 34/22, 13/34


# prueba9
