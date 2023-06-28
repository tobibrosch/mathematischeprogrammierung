import pygame
import random
from math import sqrt
import csv
from rgbcsv import color_tupels
from math import sin, cos, pi
class moving_bar:
    def __init__(self, x, y,width,heigth,length,y_offset):
        self.x = x
        self.y = y
        self.lenght = length
        self.widht=width
        self.height=heigth
        self.y_offset = y_offset
        self.text_movingbar_x = 0
        self.text_movingbar = False
        self.timer_1 = 0
        self.timer_2 = 0
    
    def update(self):
        self.timer_2 = pygame.time.get_ticks()
        rect=pygame.Rect(self.x,self.y,self.widht,self.height)
        mouse_rect = mouse_location()

        if rect.colliderect(mouse_rect):
            if self.text_movingbar and self.text_movingbar_x < self.lenght:
                self.timer_1 = pygame.time.get_ticks()
                self.text_movingbar = False
            
            if self.timer_2 - self.timer_1 > 0.01  and not self.text_movingbar:
                self.text_movingbar = True
                self.text_movingbar_x += 8
            
        else:
            if self.text_movingbar and self.text_movingbar_x > 0:
                self.timer_1 = pygame.time.get_ticks()
                self.text_movingbar = False
                

            if self.timer_2 - self.timer_1 > 0.01 and not self.text_movingbar and self.text_movingbar_x>0:
                self.text_movingbar = True
                self.text_movingbar_x -= 8

        pygame.draw.rect(screen,'white',pygame.Rect(self.x,self.y+self.y_offset,self.text_movingbar_x,5),border_radius=5)        

class formation_rects():
    def __init__(self,x_tupel,y_tupel):
        self.color = 'white'
        self.x_tupel =x_tupel
        self.y_tupel =y_tupel
        self.selected = False
    def get_formation_rect(self):
        return pygame.Rect(self.x_tupel*60+215,self.y_tupel*50+25,50,15)
    def draw_formation_rect(self):
        rect = pygame.Rect(self.x_tupel*60+215,self.y_tupel*50+25,50,15)
        if self.selected:
            self.color='purple'
        elif not self.selected:
            self.color='white'
        pygame.draw.rect(screen,self.color,rect)
    def formation_tupel(self):
        return (self.x_tupel,self.y_tupel)

class rotating_letter():
    def __init__(self,letter,starting_angle,color,radius):
        self.letter = letter
        self.starting_angle = starting_angle
        self.color = color
        self.radius = radius
        self.font = pygame.font.Font(None, 36)

    def show_rotating_letter(self):
        letter_x = 450 - int(self.radius* sin(2*pi*(text_rotation_angle-self.starting_angle)/360))
        letter_y = 500 - int(self.radius* cos(2*pi*(text_rotation_angle-self.starting_angle)/360))

        letter_show = self.font.render(self.letter, True, self.color)

        letter_rect = letter_show.get_rect()
        
        letter_rect.center=(letter_x,letter_y)
        
        letter_rotated = pygame.transform.rotate(letter_show,text_rotation_angle-self.starting_angle)

        letter_rotated_rect = letter_rotated.get_rect(center=letter_rect.center)

        screen.blit(letter_rotated,letter_rotated_rect)


    



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
        rect = pygame.Rect(self.x_position,self.y_position,self.x_size,self.y_size)
        if self.hit_counter==0:
            rectangle_color="white"
        if self.hit_counter==1:
            rectangle_color="purple"
        if self.hit_counter==2:
            rectangle_color="green"
        if self.hit_counter==3:
            rectangle_color="yellow"
        pygame.draw.rect(screen, rectangle_color ,rect)


class balls():
    def __init__(self, x_position_ball, y_position_ball, x_size, y_size, x_speed,y_speed,dx,dy,surface,colors):
        self.x_size = x_size
        self.y_size = y_size 
        self.x_position_ball = x_position_ball
        self.y_position_ball = y_position_ball
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.dx = dx
        self.dy = dy
        self.surface = surface
        self.colors = colors
    def draw_ball(self,dt):
        self.y_position_ball += self.y_speed * dt * self.dy
        self.x_position_ball += self.x_speed * dt * self.dx
        ball_rect = pygame.Rect(self.x_position_ball, self.y_position_ball, self.x_size, self.y_size)
        pygame.draw.rect(self.surface, self.colors, ball_rect)
    def get_ball(self):
        return pygame.Rect(self.x_position_ball, self.y_position_ball, self.x_size, self.y_size)

def removing_rects(rect):
    global points
    if rect!=floor:
        if rect.hit_counter==1:
            rect_test_list.remove(rect)  # Entferne das Rechteck aus der Liste
        else:
            rect_hit_new = rect.hit_counter-1
            new_rect_to_append = rect
            new_rect_to_append.hit_counter = rect_hit_new
            rect_test_list.remove(rect)
            rect_test_list.append(new_rect_to_append)
        points+=20

def moving_rect(dt):
    global lives, points, rect_test_list, ball_list_class,timer_floor_1,change_color_floor, game_state
    for ball in ball_list_class:
        if ball.get_ball().top < 0:
            ball.y_position_ball=0
            ball.y_speed*= -1
        if ball.get_ball().bottom > 710:
            ball_list_class.remove(ball)
            floor.x_position=350
            if ball_list_class==[]:
                ball_list_class.append(balls(400,400,10,10,0,ball.y_speed,0,1,screen,random.choice(ball_colors)))
                lives-=1
                if lives<=0:
                     game_state='game_over'
        elif ball.get_ball().left < 0 or ball.get_ball().right > 800:
            ball.x_speed *= -1
            if ball.get_ball().left<0:
                ball.x_position_ball=0
            if ball.get_ball().right >800:
                ball.x_position_ball=790
        ball.draw_ball(dt)
    hitbox = 10
    for rect in rect_test_list:
        for ball in ball_list_class:
            if ball.get_ball().colliderect(rect.get_rectangle()):
                '''
                if rect!=floor:
                    if rect.hit_counter==1:
                        rect_test_list.remove(rect)  # Entferne das Rechteck aus der Liste
                    else:
                        rect_hit_new = rect.hit_counter-1
                        new_rect_to_append = rect
                        new_rect_to_append.hit_counter = rect_hit_new
                        rect_test_list.remove(rect)
                        rect_test_list.append(new_rect_to_append)
                    points+=20
                '''
                if rect==floor:
                    timer_floor_1 = pygame.time.get_ticks()
                    change_color_floor=True
                    if ball.x_speed==0:
                        ball.x_speed=ball.y_speed*random.choice([-1,1])
                    ball.dy = random.randint(5,9)/10
                    ball.dx = round(sqrt(1-ball.dy**2),6)
                    ball.y_position_ball=floor.y_position-ball.y_size
                if abs(ball.get_ball().bottom - rect.get_rectangle().top) < hitbox and ball.y_speed > 0:
                    removing_rects(rect)
                    ball.y_position_ball=rect.get_rectangle().top-ball.y_size
                    ball.y_speed *= -1
                elif abs(ball.get_ball().top - rect.get_rectangle().bottom) < hitbox and ball.y_speed < 0:
                    removing_rects(rect)
                    ball.y_position_ball=rect.get_rectangle().bottom
                    ball.y_speed *= -1
                elif abs(ball.get_ball().left - rect.get_rectangle().right) < hitbox and ball.x_speed < 0:
                    removing_rects(rect)
                    ball.x_position_ball=rect.get_rectangle().right
                    ball.x_speed *= -1
                elif abs(ball.get_ball().right - rect.get_rectangle().left) < hitbox and ball.x_speed > 0:
                    removing_rects(rect)
                    ball.x_position_ball=rect.get_rectangle().left+ball.x_size
                    ball.x_speed *= -1
pygame.init()


space_bar = False
screen = pygame.display.set_mode((900, 800))
screen_width = screen.get_width()   
screen_height = screen.get_height()
clock = pygame.time.Clock()


#Schrift und Bild 
image = pygame.image.load("lose.jpeg")
image_settings=pygame.image.load("settings.jpeg")
image_settings=pygame.transform.scale(image_settings, (40, 40))
heart = "heart.gif"
heart_surface = pygame.image.load(heart)
heart_surface = pygame.transform.scale(heart_surface, (30, 20))
image_width = image.get_width()
image_height = image.get_height()
image_x = (screen_width - image_width) // 2  
image_y = (screen_height - image_height) // 2
# weißer rahmen!
frame_set = pygame.Rect(0,0,800,740)


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

def mouse_location():
    mouse_x_pos,mouse_y_pos=pygame.mouse.get_pos()
    return pygame.Rect(mouse_x_pos,mouse_y_pos,1,1)



#scoreboard 

with open('scoreboard.csv', mode='a', newline='') as file:
   writer = csv.writer(file) 

#rechtecke

floor = rectangles(100,10,350,700,0)
rect_test_list = [rectangles(90,35,i*100+5,j*40+5,random.randint(1,3)) for i in range(8) for j in range(5)]
rect_test_list.append(floor)

formation_1 = [(3,0),(4,0),(1,1),(2,1),(5,1),(6,1),(0,2),(1,2),(2,2),(5,2),(6,2),(7,2),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3)]
rect_test_list=[rectangles(90,35,100*i+5,40*j+5,random.randint(1,3)) for i,j in formation_1 ]
rect_test_list.append(floor)


formation_list = [formation_rects(x,y) for x in range(8) for y in range(5)]
seleceted_formation_list=[]
formation_safed=False

points=0
timer_floor_1=1
lives=3
one_run = 1 
name=""
name_left=True
difficulty_level='easy'
floor_x_speed=600
running = True
moving_text_menu=True
moving_text_game=True
change_color_floor=False
color_red=252
color_green=0
color_blue=0
snake_x=0
snake_y=0
x_text_moving_menu=0
x_text_moving_game=0
x_text_moving_loosing = 0
moving_text_loosing=True
#Bälle
ball_1 =  balls(390,300,10,10,0,700,0,1,screen,'red')
ball_2 =  balls(390,200,10,10,0,400,0,1,screen,'red')
ball_4 =  balls(370,200,10,10,0,400,0,1,screen,'red')
ball_3 =  balls(390,20,10,10,300,-300,0.6,0.8,screen,'red')
ball_colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "White", "Pink", "Brown", "Cyan", "Magenta", "Gray", "Lime", "Teal", "Silver", "Gold", "Indigo", "Maroon", "Navy"]

ball_list_class = [ball_1]
ball_list_menu = [ball_3]

game_state='menu'

text_movingbar=True
text_movingbar_x=0
text_movingbar_x_2=0
color_tupel_index =0
color_tupel_index_start =0
snake_list = [pygame.Rect(i*10,0,10,10) for i in range(90)] + [pygame.Rect(890,10+i*10,10,10) for i in range(79)]+[pygame.Rect(890-i*10,790,10,10) for i in range(89)]+[pygame.Rect(0,790-i*10,10,10) for i in range(79)]
rainbow_moving = True

moving_bar_1 = moving_bar(310,111,90,34,80,40)
moving_bar_2 = moving_bar(480,111,138,34,138,40)
moving_bar_3 = moving_bar(713,111,75,34,75,40)
moving_bar_4 = moving_bar(42,408,290,34,290,40)
moving_bar_5 = moving_bar(42,508,290,34,278,40)
#roation
text_rotation_aktivated=True
text_rotation_angle=0
radius_aktive=False
radius_increase=0
timer_radius_aktive=True
shrinking_radius=False
while running:
    #print(pygame.mouse.get_pos())
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
            running = False
        if game_state=='menu':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and name!='':
                    name = name[:-1]
                elif event.key != pygame.K_RETURN and event.key != (pygame.K_BACKSPACE or pygame.K_ESCAPE) and (event.unicode.isalpha() or event.key==pygame.K_SPACE):
                    name += event.unicode
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_c and game_state=='pause':
                game_state='game'
            if event.key == pygame.K_SPACE and game_state=='game':
                ball_list_menu=[ball_3]
                game_state='pause'
            if event.key == pygame.K_t and (game_state=='game_over' or game_state=='game_won'):
                ball_list_class = [ball_1]
                rect_test_list = [rectangles(90,35,i*100+5,j*40+5,random.randint(1,3)) for i in range(8) for j in range(5)]
                rect_test_list.append(floor)
                floor.x_position=350
                points=0
                lives=4
                game_state='game'

        if event.type == pygame.MOUSEBUTTONDOWN and game_state=='menu':
            if mouse_location().colliderect(pygame.Rect(10,750,40,40)):
                game_state='menu+settings'
            if mouse_location().colliderect(pygame.Rect(400,470,100,60)) and not name_left:
                shrinking_radius=True
    
        if event.type == pygame.MOUSEBUTTONDOWN and game_state=='menu+settings':
            if mouse_location().colliderect(pygame.Rect(730,745,100,30)):
                game_state='menu'
            if mouse_location().colliderect(pygame.Rect(300,100,130,40)):
                difficulty_level='easy'
            if mouse_location().colliderect(pygame.Rect(480,100,150,40)):
                difficulty_level='medium'
            if mouse_location().colliderect(pygame.Rect(700,100,100,40)):
                difficulty_level='hard'
            if mouse_location().colliderect(pygame.Rect(40,500,278,40)):
                game_state='menu+settings+formation'
        if event.type == pygame.MOUSEBUTTONUP and game_state=='menu+settings':
             if mouse_location().colliderect(pygame.Rect(40,400,300,40)):
                with open('scoreboard.csv', mode='w', newline='') as file:
                    writer = csv.writer(file) 

        if event.type == pygame.MOUSEBUTTONUP and game_state=='menu+settings+formation':
            if mouse_location().colliderect(pygame.Rect(730,745,100,30)):
                game_state='menu+settings'
            for formation_rect in formation_list:
                if mouse_location().colliderect(formation_rect.get_formation_rect()) and not formation_rect.selected and formation_rect.formation_tupel() not in seleceted_formation_list:
                    formation_rect.selected=True
                    seleceted_formation_list.append(formation_rect.formation_tupel())
                elif mouse_location().colliderect(formation_rect.get_formation_rect()) and formation_rect.selected and formation_rect.formation_tupel() in seleceted_formation_list:
                    formation_rect.selected=False
                    seleceted_formation_list.remove(formation_rect.formation_tupel())
            if mouse_location().colliderect(pygame.Rect(413,363,77,40)) and not formation_safed:
                formation_safed=True
            elif mouse_location().colliderect(pygame.Rect(413,363,77,40)) and formation_safed:
                formation_safed=False
            
    
    if radius_increase<-500 and game_state=='menu':
        game_state='game'

    if name.strip()=='':
        name_left=True
    else:   
        name_left=False 
    
    if difficulty_level=='easy' and game_state=='menu+settings':
        floor_x_speed=600
        floor.x_size=100
    if difficulty_level=='medium' and game_state=='menu+settings':
        floor_x_speed=500
        floor.x_size=50
    if difficulty_level=='hard' and game_state=='menu+settings':
        floor_x_speed=400
        floor.x_size=25
    
    
    if lives >0 and rect_test_list==[floor]:
        game_state='game_won'            
    if formation_safed and seleceted_formation_list!=[] and game_state=='menu+settings+formation':     
        rect_test_list=[rectangles(90,35,100*i+5,40*j+5,random.randint(1,3)) for i,j in seleceted_formation_list]
        rect_test_list.append(floor)

    if game_state=='menu':
        dt = 0.001
        screen.fill("black")
        for ball in ball_list_menu:
            if ball.x_position_ball >900 or ball.x_position_ball<0:
                if len(ball_list_menu)<30:
                    ball_list_menu.append(balls(random.randint(100,800),random.randint(100,800),10,10,random.choice([-1,1])*300,random.choice([-1,1])*300,0.6,0.8,screen,random.choice(ball_colors)))
                ball.x_speed*=-1
            if ball.y_position_ball >800 or ball.y_position_ball<0:
                if len(ball_list_menu)<30:
                    ball_list_menu.append(balls(random.randint(100,800),random.randint(100,800),10,10,random.choice([-1,1])*300,random.choice([-1,1])*300,0.6,0.8,screen,random.choice(ball_colors)))
                ball.y_speed*=-1
            ball.draw_ball(dt)

        #mr worldwide
        text_rotation_timer_1 = pygame.time.get_ticks()

    
        letter_ring = [rotating_letter(letter_chose,angle,'white',100) for letter_chose,angle in [('W', 0), ('e', 10), ('l', 20), ('c', 30), ('o', 40), ('m', 50), ('e', 60), ('t',72), ('o',78),('B', 90), ('r', 100), ('e', 110), ('a', 120), ('k', 130), ('o', 140), ('u', 150), ('t', 160),('W', 180), ('e', 190), ('l', 200), ('c', 210), ('o', 220), ('m', 230), ('e', 240),('t',252),('o',258),('B', 270), ('r', 280), ('e', 290), ('a', 300), ('k', 310), ('o', 320), ('u', 330), ('t', 340)]]
        #pygame.draw.circle(screen, 'white', (450,500), 100, 1)
        timer_radius_1=pygame.time.get_ticks()
        for letters in letter_ring:
            letters.color=(color_green,color_red,color_blue)
            letters.radius=100+radius_increase
            letters.show_rotating_letter()

        
        if radius_aktive and not shrinking_radius:
                timer_radius_1=pygame.time.get_ticks()
                if timer_radius_aktive and radius_increase<180:
                    timer_radius_2=pygame.time.get_ticks()
                    timer_radius_aktive=False
                    letters.radius=100+radius_increase
                    radius_increase+=1
                if timer_radius_1-timer_radius_2>10:
                    timer_radius_aktive=True
        elif radius_increase>=0 and not shrinking_radius:
            radius_increase-=2
        elif shrinking_radius:
            radius_increase-=7
        


        if text_rotation_aktivated:
            text_rotation_timer_2=pygame.time.get_ticks()
            text_rotation_aktivated=False
            text_rotation_angle+=1
        if text_rotation_timer_1-text_rotation_timer_2>2:
            text_rotation_aktivated=True
       
        #new lines 
        timer_1 = pygame.time.get_ticks()
        text(font='Arial',font_size=50,text='Welcome to Breakout',x_position=450+x_text_moving_menu,y_position=60,color=(color_red,color_green,color_blue))
        text(font='Arial',font_size=50,text='Welcome to Breakout',x_position=-450+x_text_moving_menu,y_position=60,color=(color_red,color_green,color_blue))
        
        
        if moving_text_menu == True:
            timer_2 = pygame.time.get_ticks()
            moving_text_menu=False
            if color_red==252 and color_green==0 and color_blue>=0 and color_blue<252:
                color_blue+=1
            if color_red<=252 and color_blue==252 and color_green==0 and color_red>0:
                color_red-=1
            if color_red==0 and color_blue==252 and color_green<252:
                color_green+=1
            if color_red==0 and color_green==252 and color_blue<=252 and color_blue>0:
                color_blue-=1
            if color_red>=0 and color_green==252 and color_blue==0 and color_red<252:
                color_red+=1
            if color_red==252 and color_green<=252 and color_green>0 and color_blue==0:
                color_green-=1
            x_text_moving_menu+=3


        if timer_1 - timer_2 >=5:
             moving_text_menu=True
        if x_text_moving_menu>900:
             x_text_moving_menu=-1
        text(font_size=20,text='enter name',x_position=450,y_position=250)
        rectangles(400,5,250,350,0).draw_rectangles()

        text(font_size=50,text=name.strip(),x_position=450,y_position=300,centering=True,color=(255,0,200))
        if name_left:
            text(font_size=50,text='name is missing',x_position=450,y_position=300,centering=True)
        if mouse_location().colliderect(pygame.Rect(10,750,35,35)):
            image_settings=pygame.image.load("settings.jpeg")
            image_settings=pygame.transform.scale(image_settings, (45, 45))
            y=image_settings.get_height()
            x=image_settings.get_width()
        else:
            image_settings=pygame.image.load("settings.jpeg")
            image_settings=pygame.transform.scale(image_settings, (40, 40))
            y=image_settings.get_height()
            x=image_settings.get_width()
        
        if mouse_location().colliderect(pygame.Rect(392,479,120,50)) and not shrinking_radius:
                text(font_size=50,text='start',x_position=450,y_position=500,color=(255,20,200))
                radius_aktive=True
        elif not mouse_location().colliderect(pygame.Rect(392,479,120,50)) and not shrinking_radius:
            text(font_size=60,text='start',x_position=450,y_position=500,color=(255,20,200))
            radius_aktive=False
        

        screen.blit(image_settings,(30-x/2,770-y/2))


        timer_rainbow_1 = pygame.time.get_ticks()
        if rainbow_moving:
            timer_rainbow_2= pygame.time.get_ticks()
            color_tupel_index+=1
            rainbow_moving=False
        for snake in snake_list:
            pygame.draw.rect(screen,color_tupels[color_tupel_index],snake)
            color_tupel_index+=1
            if color_tupel_index>338:
                color_tupel_index=0
        if timer_rainbow_1-timer_rainbow_2>1000:
            rainbow_moving=True

    
    if game_state=='menu+settings':
        screen.fill("black")

        text(font_size=50,text='settings',x_position=450,y_position=40)
        if mouse_location().colliderect(pygame.Rect(730,745,100,30)):
            text(font_size=40,text='menu',x_position=780,y_position=760)
        else:
            text(font_size=30,text='menu',x_position=780,y_position=760)
        
        if mouse_location().colliderect(pygame.Rect(40,400,300,40)):
            text(font_size=40,text='reset scoreboard',x_position=40,y_position=400,centering=False,color=(255,0,200))
        else:
            text(font_size=40,text='reset scoreboard',x_position=40,y_position=400,centering=False)
        if mouse_location().colliderect(pygame.Rect(40,500,278,40)):
            text(font_size=40,text='select formation',x_position=40,y_position=500,centering=False,color=(255,0,200))
        else:
            text(font_size=40,text='select formation',x_position=40,y_position=500,centering=False)


        text(font_size=40,text='difficulty level:',x_position=40,y_position=100,centering=False)

        if mouse_location().colliderect(pygame.Rect(300,100,130,40)) or difficulty_level=='easy':
            text(font_size=40,text='easy',x_position=350,y_position=120,centering=True,color=(255,0,100))
            if mouse_location().colliderect(pygame.Rect(300,100,130,40)):
                text(font_size=30,text='floorsize = 100 px and floorspeed = 600',x_position=450,y_position=300,centering=True,color=(255,0,100))
        else:
            text(font_size=40,text='easy',x_position=350,y_position=120,centering=True)

        if mouse_location().colliderect(pygame.Rect(480,100,150,40)) or difficulty_level=='medium':
            text(font_size=40,text='medium',x_position=550,y_position=120,centering=True,color=(255,0,100))
            if mouse_location().colliderect(pygame.Rect(480,100,150,40)):
                text(font_size=30,text='floorsize = 50 px and floorspeed = 500',x_position=450,y_position=300,centering=True,color=(255,0,100))
        else:
            text(font_size=40,text='medium',x_position=550,y_position=120,centering=True)
        if mouse_location().colliderect(pygame.Rect(700,100,150,40)) or difficulty_level=='hard':
             text(font_size=40,text='hard',x_position=750,y_position=120,centering=True,color=(255,0,100))
             if mouse_location().colliderect(pygame.Rect(700,100,150,40)):
                text(font_size=30,text='floorsize = 25 px and floorspeed = 400',x_position=450,y_position=300,centering=True,color=(255,0,100))
        else:
             text(font_size=40,text='hard',x_position=750,y_position=120,centering=True)
        frame_setting= pygame.Rect(0,0,900,800)
        pygame.draw.rect(screen,'white',frame_setting,5,border_radius=10)

        

        timer_rainbow_1 = pygame.time.get_ticks()
        if rainbow_moving:
            timer_rainbow_2= pygame.time.get_ticks()
            color_tupel_index+=1
            rainbow_moving=False
        for snake in snake_list:
            pygame.draw.rect(screen,color_tupels[color_tupel_index],snake)
            color_tupel_index+=1
            if color_tupel_index>337:
                color_tupel_index=0
        if timer_rainbow_1-timer_rainbow_2>10:
            rainbow_moving=True
    

    
        moving_bar_1.update()
        moving_bar_2.update()
        moving_bar_3.update()
        moving_bar_4.update()
        moving_bar_5.update()


    if game_state=='menu+settings+formation':
        screen.fill("black")
        if mouse_location().colliderect(pygame.Rect(730,745,100,30)):
            text(font_size=40,text='back',x_position=780,y_position=760)
        else:
            text(font_size=30,text='back',x_position=780,y_position=760)
        
        [formation_list[i].draw_formation_rect() for i in range(len(formation_list))]
        if mouse_location().colliderect(pygame.Rect(413,363,77,40)) or formation_safed:
            text(font_size=40,text='safe',x_position=450,y_position=380,color=(255,0,200))
        else:
            text(font_size=40,text='safe',x_position=450,y_position=380)


        timer_rainbow_1 = pygame.time.get_ticks()
        if rainbow_moving:
            timer_rainbow_2= pygame.time.get_ticks()
            color_tupel_index+=1
            rainbow_moving=False
        for snake in snake_list:
            pygame.draw.rect(screen,color_tupels[color_tupel_index],snake)
            color_tupel_index+=1
            if color_tupel_index>338:
                color_tupel_index=0
        if timer_rainbow_1-timer_rainbow_2>1000:
            rainbow_moving=True

    if game_state=='game':      
        screen.fill("black")
        pygame.draw.rect(screen,"white",frame_set,5)
        dt = 0.005
        if pressed_keys[pygame.K_a] and floor.get_rectangle().left > 0:
            floor.x_position  -= floor_x_speed * dt
        if floor.get_rectangle().left<0:
                 floor.x_position=0
        if pressed_keys[pygame.K_d] and floor.get_rectangle().right < 800:
            floor.x_position += floor_x_speed * dt
        if floor.get_rectangle().right>800:
                floor.x_position=800-floor.x_size
        for brick in rect_test_list:
             brick.draw_rectangles()

        timer_floor_2 = pygame.time.get_ticks()
        moving_rect(dt)
        if change_color_floor==True:
             floor.hit_counter=1
        if timer_floor_2-timer_floor_1>200:
             change_color_floor=False
             floor.hit_counter=0


        #Leben
        for i in range(lives):
            screen.blit(heart_surface,(800+i*33,40))
        text(font_size=30,text='Lives',x_position=850,y_position=15)
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
        timer_1 = pygame.time.get_ticks()
        text(font='Arial',font_size=30,text='press spacebar to pause game or esc to quit',x_position=450+x_text_moving_game,y_position=775)
        text(font='Arial',font_size=30,text='press spacebar to pause game or esc to quit',x_position=-450+x_text_moving_game,y_position=775)
        if moving_text_game == True:
            timer_2 = pygame.time.get_ticks()
            moving_text_game=False
            x_text_moving_game+=3
        if timer_1 - timer_2 >=5:
             moving_text_game=True
        if x_text_moving_game>900:
             x_text_moving_game=-1
        
       
    if game_state=='game_over':
        screen.fill("Black")
        text(font_size=50,text='press t to play again or esc to quit',x_position=450,y_position=450)
        if lives==0:
            with open('scoreboard.csv', mode='a', newline='') as file:
                            writer = csv.writer(file) 
                            writer.writerow([name.strip(),points])
        lives=-1
        timer_loosing= pygame.time.get_ticks()
        text(font='Arial',font_size=30,text='You Lose'+' '*20+'You Lose',x_position=450+x_text_moving_loosing,y_position=775)
        text(font='Arial',font_size=30,text='You Lose'+' '*20+'You Lose',x_position=-450+x_text_moving_loosing,y_position=775)
        text(font='Arial',font_size=30,text='You Lose'+' '*20+'You Lose',x_position=450+x_text_moving_loosing,y_position=25)
        text(font='Arial',font_size=30,text='You Lose'+' '*20+'You Lose',x_position=-450+x_text_moving_loosing,y_position=25)
        if moving_text_loosing == True:
            timer_loosing_2 = pygame.time.get_ticks()
            moving_text_loosing=False
            x_text_moving_loosing+=3
        if timer_loosing- timer_loosing_2 >=5:
             moving_text_loosing=True
        if x_text_moving_loosing>900:
             x_text_moving_loosing=-1
        timer_rainbow_1 = pygame.time.get_ticks()
        if rainbow_moving:
            timer_rainbow_2= pygame.time.get_ticks()
            color_tupel_index+=1
            rainbow_moving=False
        for snake in snake_list:
            pygame.draw.rect(screen,color_tupels[color_tupel_index],snake)
            color_tupel_index+=1
            if color_tupel_index>337:
                color_tupel_index=0
        if timer_rainbow_1-timer_rainbow_2>10:
            rainbow_moving=True

    if game_state=='game_won':
        screen.fill("Black")
        text(font_size=50,text='Nice you won!',x_position=450,y_position=450)
        text(font_size=50,text='you have gained. '+str(points)+' points!',x_position=450,y_position=500)
        text(font_size=50,text='If you want to play again',x_position=450,y_position=550)
        text(font_size=50,text='press t or esc to quit the game!',x_position=450,y_position=600)
        if one_run==1:
            with open('scoreboard.csv', mode='a', newline='') as file:
                            writer = csv.writer(file) 
                            writer.writerow([name.strip(),points])
        
        one_run+=1
        timer_rainbow_1 = pygame.time.get_ticks()
        if rainbow_moving:
            timer_rainbow_2= pygame.time.get_ticks()
            color_tupel_index+=1
            rainbow_moving=False
        for snake in snake_list:
            pygame.draw.rect(screen,color_tupels[color_tupel_index],snake)
            color_tupel_index+=1
            if color_tupel_index>337:
                color_tupel_index=0
        if timer_rainbow_1-timer_rainbow_2>10:
            rainbow_moving=True
    if game_state=='pause':
        screen.fill("Black")
        for ball in ball_list_menu:
            if ball.x_position_ball >900 or ball.x_position_ball<0:
                if len(ball_list_menu)<300:
                    ball_list_menu.append(balls(random.randint(100,800),random.randint(100,800),10,10,random.choice([-1,1])*300,random.choice([-1,1])*300,0.6,0.8,screen,random.choice(ball_colors)))
                ball.x_speed*=-1
            if ball.y_position_ball >800 or ball.y_position_ball<0:
                if len(ball_list_menu)<300:
                    ball_list_menu.append(balls(random.randint(100,800),random.randint(100,800),10,10,random.choice([-1,1])*300,random.choice([-1,1])*300,0.6,0.8,screen,random.choice(ball_colors)))
                ball.y_speed*=-1
            ball.draw_ball(0.005)
        text(font_size=30,text='Points: '+str(points),x_position=450,y_position=400)
        text(font_size=30,text='press c to continue or esc for quit',x_position=450,y_position=450)
        timer_rainbow_1 = pygame.time.get_ticks()
        if rainbow_moving:
            timer_rainbow_2= pygame.time.get_ticks()
            color_tupel_index+=1
            rainbow_moving=False
        for snake in snake_list:
            pygame.draw.rect(screen,color_tupels[color_tupel_index],snake)
            color_tupel_index+=1
            if color_tupel_index>338:
                color_tupel_index=0
        if timer_rainbow_1-timer_rainbow_2>10:
            rainbow_moving=True
    clock.tick(120)
    pygame.display.flip()
pygame.quit()