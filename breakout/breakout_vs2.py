import pygame
import random
from math import sqrt
import csv

class rectangles():
    def __init__(self,x_size,y_size,x_position,y_position,hit_counter):
        self.x_size = x_size
        self.y_size = y_size
        self.x_position = x_position
        self.y_position = y_position
        self.hit_counter = hit_counter
    def get_rectangle(self):
        return pygame.Rect(self.x_position,self.y_position,self.x_size,self.y_size)
    def draw_rectangles(self):
        print("draw rectangles")
        rect = pygame.Rect(self.x_position,self.y_position,self.x_size,self.y_size)
        if self.hit_counter==1:
            rectangle_color="purple"
        if self.hit_counter==2:
            rectangle_color="green"
        if self.hit_counter==3:
            rectangle_color="yellow"
        pygame.draw.rect(screen, rectangle_color ,rect)
    def hits(self):
        print(self.hit_counter)

def moving_rect(dt):
    global x_speed, y_speed,rectangle_list,dx,dy,lives, points
    rect_1.x += x_speed * dt * dx
    rect_1.y += y_speed * dt * dy
    pygame.draw.rect(screen, "red", rect_1)
    pygame.draw.rect(screen, "white", rect_2)
    if rect_1.top < 0:
        y_speed *= -1
    if rect_1.bottom > 800:
        x_speed=0
        rect_1.x, rect_1.y = 400, 400
        lives-=1
    elif rect_1.left < 0 or rect_1.right > 800:
        x_speed *= -1
        if rect_1.left<0:
             rect_1.left=0
        if rect_1.right >800:
             rect_1.right=800
    hitbox = 4
    for rect in rectangle_list:
        if rect_1.colliderect(rect):
            if rect!=rect_2:
                rectangle_list.remove(rect)  # Entferne das Rechteck aus der Liste
                points+=20
            if rect==rect_2:
                if x_speed==0:
                    x_speed=400*random.choice([-1,1])
                dy = random.randint(5,9)/10
                dx = round(sqrt(1-dy**2),4)
                rect_1.bottom=700
            if abs(rect_1.bottom - rect.top) < hitbox and y_speed > 0:
                rect_1.bottom=rect.top
                y_speed *= -1
            elif abs(rect_1.top - rect.bottom) < hitbox and y_speed < 0:
                rect_1.top=rect.bottom
                y_speed *= -1
            elif abs(rect_1.left - rect.right) < hitbox and x_speed < 0:
                rect_1.left=rect.right
                x_speed *= -1
            elif abs(rect_1.right - rect.left) < hitbox and x_speed > 0:
                rect_1.right=rect.left
                x_speed *= -1
pygame.init()





space_bar = False
screen = pygame.display.set_mode((900, 800))
screen_width = screen.get_width()
screen_height = screen.get_height()
clock = pygame.time.Clock()
rect_1 = pygame.Rect(400, 400, 10, 10)
rect_2 = pygame.Rect(200, 700, 100, 10)

#Schrift und Bild 
image = pygame.image.load("lose.jpeg")
heart = "heart.gif"
heart_surface = pygame.image.load(heart)
heart_surface = pygame.transform.scale(heart_surface, (30, 20))
image_width = image.get_width()
image_height = image.get_height()
image_x = (screen_width - image_width) // 2  
image_y = (screen_height - image_height) // 2

#punktesystem


font_1 = pygame.font.Font(None, 50)  # Schriftart und Schriftgröße festlegen
text_1 = font_1.render("YOU LOSE!", True, (255, 255, 255))  # text_1 rendern
text_1_width = text_1.get_width()
text_1_height = text_1.get_height()
text_1_x = (screen_width - text_1_width) // 2  # x-Position für die horizontale Ausrichtung
text_1_y = (screen_height - text_1_height) // 2  # y-Position für die vertikale Ausrichtung
font_2 = pygame.font.Font(None, 36)
text_2 = font_2.render("Lives", True, (255, 255, 255))
text_2_width = text_2.get_width()
text_2_height = text_2.get_height()
text_2_x = (screen_width - text_2_width) // 2  # x-Position für die horizontale Ausrichtun
text_2_y = (screen_height - text_2_height) // 2 

def text(font='Arial',font_size=10,text='',color=(255,255,255),x_position=0,y_position=0,centering=True,scale=False,scale_x=100,scale_y=100):
   text_font = pygame.font.SysFont(font,font_size)
   text_shown = text_font.render(text, True, color)
   text_font_width = text_shown.get_width()
   text_font_height = text_shown.get_height()
   if centering:
        if not scale:
            screen.blit(text_shown,(x_position-text_font_width/2,y_position-text_font_height/2))
        else:
            text_shown = pygame.transform.scale(text_shown, (scale_x, scale_y))
            screen.blit(text_shown,(x_position-text_font_width/2,y_position-text_font_height/2))
   elif not centering:
        if not scale:
            screen.blit(text_shown,(x_position,y_position))
        else:
            text_shown = pygame.transform.scale(text_shown, (scale_x, scale_y))
            screen.blit(text_shown,(x_position,y_position))


points=0

losing_list = []
for i in range(1,10):
            losing_list.append(text_1)
#Rechtecke
rectangle_list = [pygame.Rect(i*100+5,j*25,90,20) for i in range(8) for j in range(4)]
rectangle_list.append(rect_2)
#Geschwindigkeiten
x_speed = 0
y_speed = 400
dx =1
dy =1

#Leben
lives=3
#scoreboard 
#scoreboard = [['Name','Punkte']]
with open('scoreboard.csv', mode='a', newline='') as file:
   writer = csv.writer(file) 


rect_test_list = [rectangles(90,20,i*100+5,j*25,random.randint(1,3)) for i in range(8) for j in range(4)]
one_run = 1 
name=""
input = False

running = True

menu = True

while running:
    # Beende durch X drücken oder q
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
            running = False
        if menu:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu=False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not menu:
                space_bar=True
            #test für mehrere hits 
            if event.key == pygame.K_r:
                if rect_test_list!=[]:
                    new_hit=rect_test_list[0].hit_counter-1
                    rect_to_append = rect_test_list[0]
                    rect_to_append.hit_counter = new_hit
                    rect_test_list.remove(rect_test_list[0])
                    if new_hit>0:
                        rect_test_list.insert(0,rect_to_append)
                else:
                    pass

    
    if menu:
        screen.fill("black")
        for rectto in rect_test_list:
             rectto.draw_rectangles()
    
        text(font='Arial',font_size=50,text='Welcome to Breakout',x_position=450,y_position=60)
        text(font_size=50,text='name: '+name,x_position=300,y_position=300,centering=False)
        clock.tick(120)
        pygame.display.flip()


    if lives>0 and rectangle_list!=[rect_2] and not space_bar and not menu:        
        screen.fill("black")
        dt = clock.tick(120) / 1000

        if pressed_keys[pygame.K_a] and rect_2.left > 0:
            rect_2.x -= 600 * dt
        if pressed_keys[pygame.K_d] and rect_2.right < 800:
            rect_2.x += 600 * dt

        for brick in rectangle_list:
            pygame.draw.rect(screen, "purple" ,brick)

        moving_rect(dt)
        #Leben
        for i in range(lives):
            screen.blit(heart_surface,(800+i*30,40))
        screen.blit(text_2,(800+(100-text_2_width)/2,0))
        #Punkte
        text(font_size=30,text='Points: '+str(points),centering=False,x_position=800,y_position=110,scale=True,scale_x=100,scale_y=20)
        #Scoreboard
        j=0
        text(font_size=30,text='Scoreboard',centering=False, x_position=800,y_position=160,scale=True,scale_x=100,scale_y=20)
        
        with open('scoreboard.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                j+=1
                text(font_size=30,text=row[0]+' '+row[1],scale=True,centering=False,scale_x=100,scale_y=20,x_position=800,y_position=160+j*30)
        j=0

        text(font_size=30,text='press spacebar to pause game or esc to quit',x_position=450,y_position=750)
        pygame.display.flip()
        clock.tick(120)

    if lives<=0:
        screen.fill("Black")
        screen.blit(text_1,(text_1_x,text_1_y))
        for text_1_1 in losing_list:
            random.randint(0,800)
            screen.blit(text_1_1,(random.randint(0,800),random.randint(0,800)))
        if lives==0:
            with open('scoreboard.csv', mode='a', newline='') as file:
                            writer = csv.writer(file) 
                            writer.writerow([str(name),points])
        lives-=1
        screen.blit(image,(image_x,image_y))
        pygame.time.delay(200)
        clock.tick(120)
        pygame.display.flip()
    if rectangle_list == [rect_2] and lives >0:
        screen.fill("Black")
        text(font_size=50,text='Nice you won!',x_position=450,y_position=450)
        text(font_size=50,text=str(points),x_position=450,y_position=500)
        if one_run==1:
            with open('scoreboard.csv', mode='a', newline='') as file:
                            writer = csv.writer(file) 
                            writer.writerow([str(name),points])
        one_run+=1
        clock.tick(120)
        pygame.display.flip()
    if space_bar and lives>0 and not menu:  
        if pressed_keys[pygame.K_c]:
            space_bar=False
        screen.fill("Black")
        text_line1 = font_2.render("Points: " + str(points), True, (255, 255, 255))
        text_line2 = font_2.render("press c to continue or esc for quit", True, (255, 255, 255))
        screen.blit(text_line1, (380, 400))
        screen.blit(text_line2, (250, 430))
        clock.tick(120)
        pygame.display.flip()
pygame.quit()
