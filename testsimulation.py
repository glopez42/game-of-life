from algorithm.simulation import Simulation
from rule import Rule
from data import dbManager

rule = Rule(dbManager.getRuleByName("prueba3"))
sim = Simulation(200, 200, 200, rule.getRule())
parameters = sim.runSimulation()

n1 = parameters["N1"]
n2 = parameters["N2"]
m1 = parameters["M1"]
m2 = parameters["M2"]
L = parameters["L"]
c1 = parameters["C1"]
S1 = (n1 - n2 +  L) / L
S2 = (m1 - m2 + L) / L
f = (S1 * S2) / c1

print(parameters, f)