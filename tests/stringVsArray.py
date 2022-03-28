import sys
import random
import time as t

# Creamos string y array de 512 posiciones con valores aleatorios

bits = 512

ruleString = ""

for n in range(bits):
    c = random.choice([0,1])
    c = str(c)
    ruleString += c

# print(ruleString)

ruleArray = [random.choice([0,1]) for e in range(n+1)]
# print(ruleArray)


print("\n\n------ Empezamos pruebas ------\n\n")

tiempoTotal = 0
# pruebas con string
print("Prueba con string:")

print("1) Recorrer todos los elementos 100.000 veces: ")
inicio = t.time()

for i in range(100001):
    for c in ruleString:
        aux = c

fin = t.time()

print("Tiempo: " ,fin - inicio)
tiempoTotal += fin - inicio

print("2) 10000 mutaciones aleatorias: ")

inicio = t.time()

for i in range(10001):
    pos = int(random.random() * 511)
    c = ruleString[pos]
    c = "0" if c == "1" else "1"
    ruleString = ruleString[:pos] + c + ruleString[pos + 1:]

fin = t.time()

print("Tiempo: ", fin - inicio)
tiempoTotal += fin - inicio

print("\nTiempo Total: ", tiempoTotal)

print("----- ------")

tiempoTotal = 0
# pruebas con listas
print("Prueba con lista:")

print("1) Recorrer todos los elementos 100.000 veces: ")
inicio = t.time()

for i in range(100001):
    for c in ruleArray:
        aux = c

fin = t.time()

print("Tiempo: " ,fin - inicio)
tiempoTotal += fin - inicio

print("2) 10000 mutaciones aleatorias: ")

inicio = t.time()

for i in range(10001):
    pos = int(random.random() * 511)
    c = ruleArray[pos]
    c = 0 if c == 1 else 1
    ruleArray[pos] = c

fin = t.time()

print("Tiempo: ", fin - inicio)
tiempoTotal += fin - inicio

print("\nTiempo Total: ", tiempoTotal)
