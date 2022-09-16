import universe as u
import sys
import time
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from data import dbManager
from rule import Rule
from algorithm.init import getBaysSpaceRule


if len(sys.argv) != 4:
    print("\nERROR: game.py usage: \n\npython game.py"
    + "\n\t[rule_name] "
    + "\n\t[window's dimension] "
    + "\n\t[universe's dimension]")
    exit(-1)

BLUE = [0.0, 0.0, 1.0]
GREEN = [0.0, 1.0, 0.0]
RED = [1.0, 0.0, 0.0]
YELLOW = [1.0, 1.0, 0.0]
BLACK = [0.0, 0.0, 0.0]
WHITE = [1.0, 1.0, 1.0]
GRAY = [0.15, 0.15, 0.15]
PINK = [1.0, 0.0, 1.0]
PURPLE = [0.5, 0.0, 1.0]

winColor = BLACK
gridColor = GRAY
cellColor = WHITE

# Window dimensions
dimXwindow = int(sys.argv[2])
dimYwindow = int(sys.argv[2])

# Universe dimensions
dimXgrid = int(sys.argv[3])
dimYgrid = int(sys.argv[3])

cellSize = dimXwindow / dimXgrid

# Universe's rule
try:
    lifeRule = Rule(dbManager.getRuleByName(sys.argv[1]))
    rule = lifeRule.getRule()
except:
    initialRuleName = sys.argv[1]
    splitRule = initialRuleName.split("/")
    Eb = int(splitRule[0][0])
    Eh = int(splitRule[0][1])
    Fb = int(splitRule[1][0])
    Fh = int(splitRule[1][1])
    initialRule = (Eb, Eh, Fb, Fh)
    rule = getBaysSpaceRule(initialRule).getRule()

# First state of the universe
universe = [[ 1  for i in range(dimXgrid)] for j in range(dimYgrid)]

speed = 0.1
stop = True
paintGrid = True

# Window setup
def init():
    global winColor
    glClearColor(winColor[0], winColor[1], winColor[2], 1)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D( 0, dimXwindow, -dimYwindow, 0 ) 

# Returns the cell's position on the universe
def getCell(posX, posY):
    x = int(posX / (dimXwindow / dimXgrid))
    y = int(posY / (dimYwindow / dimYgrid))
    return x,y

# Returns the real cell's position on the window
def getRealPosition(xCell, yCell):
    x = int(xCell * (dimXwindow / dimXgrid))
    y = -1 * int(yCell * (dimYwindow / dimYgrid))
    return x,y




# Draws all the living cells
def drawAliveCells():
    for j in range(dimYgrid):
        for i in range(dimXgrid):
            if universe[j][i] == 0:
                x,y = getRealPosition(i,j)
                drawSquare(x,y)
    glFlush()

def drawSquare(xPos, yPos):
    global cellColor

    glColor3fv(cellColor)
    glBegin(GL_POLYGON)
    glVertex2f(xPos, yPos)
    glVertex2f(xPos + cellSize, yPos)
    glVertex2f(xPos + cellSize, yPos - cellSize)
    glVertex2f(xPos, yPos - cellSize)
    glEnd()

# Draws a grid on the universe               
def grid():
    global paintGrid

    glColor3fv(gridColor)
    glLineWidth(0.001)
    glBegin(GL_LINES)

    saltoX = dimXwindow / dimXgrid
    saltoY = - dimYwindow / dimYgrid

    i = 0
    while i <= dimXwindow:
        glVertex2f(i,0)
        glVertex2f(i,-dimYwindow)
        i += saltoX

    j = 0
    while j >= -dimYwindow:
        glVertex2f(0,j)
        glVertex2f(dimXwindow,j)
        j += saltoY
    
    glEnd()





# Mouse and Keyboard actions
def mouseHandler(button, state, x, y):
    global universe
    global stop

    # When clicked, a cell is reborned or killed
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
        xCell, yCell = getCell(x, y)
        previousState = universe[yCell][xCell]
        universe[yCell][xCell] = 0 if previousState == 1 else 1     
    
def keyboard(key, x, y):
    global stop
    global paintGrid
    global universe
    global winColor
    global cellColor

    # Clears the universe
    if key == b'c' or key == b'C':
        universe = [[ 1  for i in range(dimXgrid)] for j in range(dimYgrid)]
    
    # Random universe generator
    elif key == b'r' or key == b'R': 
        universe = [[ random.choice([1,1,1,1,1,0]) for i in range(dimXgrid)] for j in range(dimYgrid)]
    
    # Random universe generator inside a 40x40 middle square
    elif key == b's' or key == b'S':
        centerY = int(dimYgrid/2)
        centerX = int(dimXgrid/2)
        for j in range(dimYgrid):
            for i in range(dimXgrid):
                if i >= centerX - 20 and i <= centerX + 20 and j >= centerY - 20 and j <= centerY + 20:
                    universe[j][i] = random.choice([1,1,1,0])
                else:
                    universe[j][i] = 1

    # Random universe generator inside a 10x10 middle square
    elif key == b'a' or key == b'A':
        centerY = int(dimYgrid/2)
        centerX = int(dimXgrid/2)
        for j in range(dimYgrid):
            for i in range(dimXgrid):
                if i >= centerX - 5 and i <= centerX + 5 and j >= centerY - 5 and j <= centerY + 5:
                    universe[j][i] = random.choice([1,0])
                else:
                    universe[j][i] = 1

    # Freeze the current universe state
    elif key == b' ':
        stop = not stop
    
    # Draws the grid
    elif key == b'g' or key == b'B':
        paintGrid = not paintGrid
    
    # Changes color of the automata
    elif (key == b'm' or key == b'M') and cellColor == WHITE:
        cellColor = BLACK
        winColor = WHITE
        glClearColor(winColor[0], winColor[1], winColor[2], 1)
    
    elif (key == b'm' or key == b'M') and cellColor == BLACK:
        cellColor = WHITE
        winColor = BLACK
        glClearColor(winColor[0], winColor[1], winColor[2], 1)
    
    glutPostRedisplay()

def specialKeyboard(key, x, y):
    global speed
    global universe
    global rule

    # Speeds up the game
    if key == GLUT_KEY_UP:
        speed -= speed * 0.5
    
    # Speeds down the game
    if key == GLUT_KEY_DOWN:
        speed += speed * 0.5
    
    # If the game is stopped, paints next state
    if key == GLUT_KEY_RIGHT and stop:
        universe = u.nextState(rule, universe)

    glutPostRedisplay()



def main():
    global universe
    global stop
    global rule

    glClear(GL_COLOR_BUFFER_BIT)

    if paintGrid:
        grid()

    drawAliveCells()

    if not stop:
        time.sleep(speed)
        universe = u.nextState(rule, universe)
        glutPostRedisplay()

    
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 
glutInitWindowPosition(200,200)
glutInitWindowSize(dimXwindow,dimYwindow)
glutCreateWindow(b'Game of Life')

init()

glutDisplayFunc(main) 
glutMouseFunc(mouseHandler)
glutKeyboardFunc(keyboard)
glutSpecialFunc(specialKeyboard)
glutMainLoop()







