import pygame 
import sys 

BLACK = (0,0,0)
WHITE = (255,255,255)  

# Inicializa pygame
pygame.init()    
# Resolución
res = (1080,720) 
# Creamos la pantalla
pantalla = pygame.display.set_mode(res) 

width = pantalla.get_width() 
height = pantalla.get_height() 

# Definimos la fuente
fuente = pygame.font.Font("../fonts/ARCADE.TTF", 75)
  
text = fuente.render('Conway-s Game of Life' , True , WHITE) 

textRect = text.get_rect()
textRect.center = (width // 2, height // 4.5)

while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
    # fills the screen with a color 
    pantalla.fill(BLACK) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
      
    # superimposing the text onto our button 
    pantalla.blit(text, textRect) 
      
    # updates the frames of the game 
    pygame.display.update() 