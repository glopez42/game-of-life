from algorithm.main import Algorithm
from algorithm import init
from data import dbManager
from rule import Rule
import timeit


rule = Algorithm().run()
dbManager.insertRule("prueb2", rule.getRuleList())

# prueba


