from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

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
figColor = GRAY

dimXwindow = 1000
dimYwindow = 1000

dimXgrid = 100
dimYgrid = 100

cellSize = dimXwindow / dimXgrid

cells = mat = [[0 for i in range(dimXgrid)] for j in range(dimYgrid)]

def getCell(posX, posY):
    x = int(posX / int(dimXwindow / dimXgrid))
    y = int(posY / int(dimYwindow / dimXgrid))
    return x,y

def getRealPosition(xCell, yCell):
    x = int(xCell * int(dimXwindow / dimXgrid))
    y = -1 * int(yCell * int(dimYwindow / dimYgrid))
    # y = dimYwindow - y if y >= 50 else y 
    return x,y

def drawAliveCells():
    for j in range(dimXgrid):
        for i in range(dimYgrid):
            if cells[i][j]:
                x,y = getRealPosition(i,j)
                drawSquare(x,y)


def drawSquare(xPos, yPos):
    #Color del trazo
    glColor3fv(WHITE)

    glBegin(GL_POLYGON)

    glVertex2f(xPos, yPos)
    glVertex2f(xPos + cellSize, yPos)
    glVertex2f(xPos + cellSize, yPos - cellSize)
    glVertex2f(xPos, yPos - cellSize)

    glEnd()
    glFlush()

def mouseHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON:
        xCell, yCell = getCell(x, y)

        cells[xCell][yCell] = 1
        xPos, yPos = getRealPosition(xCell, yCell)

        drawSquare(xPos, yPos)
        
        
def init(): #para inicar la ventana
    glClearColor(winColor[0], winColor[1], winColor[2], 1)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D( 0, dimXwindow, -dimYwindow, 0 ) 

def grid():
    glClear(GL_COLOR_BUFFER_BIT)

    # Indicar a OpenGL que pinte puntos
    glColor3fv(figColor)
    glLineWidth(0.001)
    glBegin(GL_LINES)

    #Por cada pareja de puntos se hace una recta

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
    glFlush() 


def main():
    grid()
    drawAliveCells()
    


glutInit(sys.argv) #Inicializa glut
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 

#Parametros de la ventana
glutInitWindowPosition(200,200) #La entrada son nº de pixeles entonces debe ser entero
glutInitWindowSize(dimXwindow,dimYwindow)
glutCreateWindow(b'Mi ventana') #Hay que poner una b antes

init()

glutDisplayFunc(main) #define que funcion se va a mostrar
glutMouseFunc(mouseHandler)
glutMainLoop()

