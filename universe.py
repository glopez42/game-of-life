
def _getContext(x, y, universe):
    height = len(universe)
    width = len(universe[0])

    # initial coordinates of the first element of the context
    xPointer = x - 1
    yPointer = y - 1


    context = []
    # to get the 9 cells
    for _ in range(3):
        for _ in range(3):
            # if the contexts are below or over the limits of the window
            if xPointer < 0 or yPointer < 0 or xPointer >= width or yPointer >= height:
                context.append(1)       
            else:         
                context.append(universe[yPointer][xPointer])
            xPointer += 1
        xPointer = x - 1
        yPointer += 1
    
    return context
        

def nextState(rule, universe):
    height = len(universe)
    width = len(universe[0])

    nextUniverse = [[1 for i in range(width)] for j in range(height)]

    # loop through the universe
    for y in range(height):
        for x in range(width):
            # for each cell we get its context and look in the rule for the next state
            context = _getContext(x, y, universe)
            state = rule.get(tuple(context))
            nextUniverse[y][x] = state

    return nextUniverse

