from data import dbManager
from rule import Rule

def aliveNeighbors(c):
    alive = 0
    # recorremos los vecinos
    for i in range(9):
        neighbor = c[i]
        # si está viva y no es la central se suma uno a los vivos
        if neighbor == 0 and i != 4:
            alive += 1
    return alive


# Bays space rule: EbEh / FbFh 
def getBaysSpaceRule() -> Rule:
	rule = []

	# Rule 35/33
	Eb = 3
	Eh = 5
	Fb = 3
	Fh = 3

	contexts = dbManager.getContexts()
	for c in contexts:
		# central cell
		cell = c[4]
		# if alive
		if cell == 0:
			alive = aliveNeighbors(c)
			if alive >= Eb and alive <= Eh:
				rule.append(0)
			else:
				rule.append(1)

		# dead
		else:
			alive = aliveNeighbors(c)
			if alive >= Fb and alive <= Fh:
				rule.append(0)
			else:
				rule.append(1)
	
	return Rule(rule)
