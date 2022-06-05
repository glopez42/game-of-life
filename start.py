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

print("\nRule saved on the database with name: " + sys.argv[2])

# Mutations
rule2 = dbManager.getRuleByName(initialRuleName)
cont = 0
for bit1, bit2 in zip(rule.getRuleList(), rule2):
    if bit1 != bit2:
        print("Mutated bit in position: ", cont)
    cont += 1
