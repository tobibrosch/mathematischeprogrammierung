import pygame
import random
import time
from math import sqrt
# Initialization
pygame.init()
clock = pygame.time.Clock()
# Window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Background color
background_color = (255, 255, 255)  # White
#Bodenplatte Farbe 
rect_color = "black"
#Anfangspositionen 
#Rechteck
rect_x_position = screen_width / 2 
#Ball 
ball_x_position = screen_width / 2 
ball_y_position = screen_height / 2 
#Initial für Abwärtsbewegung Ball 
up = False
down = True
right=False
left = False
#Leben
lives = 3
#Bodenplatte verändern des winkels mit random 
dt_x=1
dt_y=1
#Farbenwechsel zeiten
current_time=0
red_color_time=0
#Failing Bildschirm
failing_display_time=0
# Starte den Spielloop mit running
running = True
while running:
    #Beende durch X drücken oder q 
    pressed_keys = pygame.key.get_pressed()   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_keys[pygame.K_q]:
            running = False

    
    #Movement der Baseplatte mit Limit der ränder 
    if pressed_keys[pygame.K_a] and rect_x_position >=0:
        rect_x_position -= 0.5 * dt
    if pressed_keys[pygame.K_d] and rect_x_position <=screen_width-rect_size[0]:
        rect_x_position += 0.5 * dt


    screen.fill(background_color)
    #Bodenplatte 
    #position der Bodenplatte
    rect_position = pygame.Vector2(rect_x_position, 575)
    #Größe der Bodenplatte 
    rect_size = pygame.Vector2(100, 20)
    #Linienstärke = 0 bedeutet das Rechteck ist ausgefüllt.
    rect_thickness = 0 
    #Initialisieren der Bodenplatte
    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_position, rect_size))


    #Ball
    #radius = 5
    pygame.draw.circle(screen,"red",pygame.Vector2(ball_x_position,ball_y_position),5)
    # movment des Balls 

    if ball_y_position>0 and ball_y_position <600:
        if down:
            ball_y_position+=3*dt_y
        if up:
            ball_y_position-=3*dt_y
        if right:
            ball_x_position+=3*dt_x
        if left:
            ball_x_position-=3*dt_x
            
    #Kollision am Boden
    if ball_y_position >= 600:
        #reset wieder 
        ball_y_position=screen_height/2
        ball_x_position=screen_width/2
        up=False
        down=True
        left=False
        right=False
        dt_x=1
        dt_y=1
        #Leben runter zählen 
        lives-=1
        if lives ==0:
            running=False

    #Kollision an der Decke 
    if ball_y_position <= 0:
        ball_y_position+=1
        up = False
        down = True

    #Kollision an der Bodenplatte
    if ball_x_position <= rect_x_position+100 and ball_x_position >=rect_x_position and ball_y_position>=575 and ball_y_position<580:
        up=True
        down=False
        #farbenwechsel
        rect_color="green"
        red_color_time = pygame.time.get_ticks()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_d]:
            dt_y=random.randint(6,9)/10
            dt_x=round(sqrt(1-dt_y**2),4)
            print("Random wurde akiviert")
        if not right:
            left=True   
        if not left:
            right=True

    
    #Bodenplatte Farbenwechsel für 2 Sekunden
    current_time  = pygame.time.get_ticks()

    if current_time - red_color_time > 200:
        rect_color = "black"
     

    #Kollision an der rechten Wand 
    if ball_x_position <0:
        left=False
        right=True  
    #Kollision an der linken Wand
    if ball_x_position >screen_width:
        left=True
        right=False

    #Leben anhand von Rechecken 
    if lives==3:
        pygame.draw.rect(screen,"red",pygame.Rect(pygame.Vector2(10,10),pygame.Vector2(10,10)),0)
        pygame.draw.rect(screen,"red",pygame.Rect(pygame.Vector2(25,10),pygame.Vector2(10,10)),0)
        pygame.draw.rect(screen,"red",pygame.Rect(pygame.Vector2(40,10),pygame.Vector2(10,10)),0)
    if lives==2:
        pygame.draw.rect(screen,"red",pygame.Rect(pygame.Vector2(10,10),pygame.Vector2(10,10)),0)
        pygame.draw.rect(screen,"red",pygame.Rect(pygame.Vector2(25,10),pygame.Vector2(10,10)),0)
    if lives==1:
        pygame.draw.rect(screen,"red",pygame.Rect(pygame.Vector2(10,10),pygame.Vector2(10,10)),0)
    

    # fps sind 120 
    clock.tick(120)
    # Zeit für fps 
    dt = clock.tick(120)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
