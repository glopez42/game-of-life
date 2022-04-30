from algorithm.main import Algorithm
from algorithm import init
from data import dbManager
from rule import Rule
import sys

if len(sys.argv) != 4:
    print("ERROR: start.py usage: \n\npython start.py [initial_rule] [result_name] [iterations]")
    exit(-1)

iter = int(sys.argv[3])

rule = Algorithm().run(iter)
dbManager.insertRule(sys.argv[2], rule.getRuleList())

# Imprime mutaciones
rule2 = dbManager.getRuleByName(sys.argv[1])
cont = 0
for bit1, bit2 in zip(rule.getRuleList(), rule2):
    if bit1 != bit2:
        print("Mutación en bit: ", cont)
    cont += 1


# Bays space: 35/33
# Interesantes: prueba, prueb2, prueba42
# Borrar: prueba2, prueba3

# Bays space: 12/33
# Interesantes:
# Borrar: prueba4


