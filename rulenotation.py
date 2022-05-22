from data import dbManager
import sys

rule1 = dbManager.getRuleByName(sys.argv[1])
rule2 = dbManager.getRuleByName(sys.argv[2])

result = []

cont = 0
for bit1, bit2 in zip(rule1, rule2):
    if bit1 != bit2:
        result.append(cont)
    cont += 1

print(result)