#import timeit

def loop(universe, x, y):
    # getting the cell's context, 9 cells (3x3 matrix)
    xPointer = x - 1
    yPointer = y - 1
    context = []
    append = context.append
    for _ in range(3):
        for _ in range(3):
            try:
                append(universe[yPointer][xPointer])
            except:
                append(1)                   
            xPointer += 1
        xPointer = x - 1
        yPointer += 1

    return context


def nextState(rule, universe):
    
    #start2 = timeit.default_timer()
    
    height = len(universe)
    width = len(universe[0])
    
    nextUniverse = [[1] * width for _ in range(height)]

    getState = rule.get

    y = 0
    x = 0
    
    for row in universe:
        y1 = y - 1
        y2 = y + 1
        for elem in row:
            x1 = x - 1
            x2 = x + 1

            context = []
            append = context.append

            line = universe[y1]
            append(line[x1])
            append(line[x])
            try: 
                append(line[x2])
            except:
                append(line[0])

            append(row[x1])
            append(elem)
            try: 
                append(row[x2])
            except:
                append(row[0])

            try: 
                line = universe[y2]
            except:
                line = universe[0]

            append(line[x1])
            append(line[x])
            try: 
                append(line[x2])
            except:
                append(line[0])

            nextUniverse[y][x] = getState(tuple(context))
            context = []
            x += 1
                
        x = 0
        y += 1

    #stop2 = timeit.default_timer()
    #print("iter " + str(stop2 - start2) + " ")

    return nextUniverse

