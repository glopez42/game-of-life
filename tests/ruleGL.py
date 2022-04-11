from contexts import CONTEXTS


def aliveNeighbors(c):
    alive = 0
    # recorremos los vecinos
    for i in range(9):
        neighbor = c[i]
        # si está viva y no es la central se suma uno a los vivos
        if neighbor == 0 and i != 4:
            alive += 1
    return alive


rule = []

for c in CONTEXTS:
    # accedemos a la célula central
    cell = c[4]

    # si está viva
    if cell == 0:
        alive = aliveNeighbors(c)
        # si hay entre dos o tres vecinas vivas, vivirá
        if alive >= 2 and alive <= 3:
            rule.append(0)
        # en otro caso muere
        else:
            rule.append(1)

    # si esta muerta
    else:
        alive = aliveNeighbors(c)
        # si tiene 3 vecinas vivas, renacerá
        if alive == 3:
            rule.append(0)
        # en otro caso, seguirá muerta
        else:
            rule.append(1)
