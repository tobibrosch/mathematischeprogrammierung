import pygame
import random
from math import sqrt
import csv
from rgbcsv import color_tupels
from math import sin, cos, pi
import numpy as np


class moving_bar:
    def __init__(self, x, y,width,heigth,length,y_offset,rect_chosen):
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
        self.rect_chosen=rect_chosen
    def update(self):
        self.timer_2 = pygame.time.get_ticks()
        if self.rect_chosen == None:
            rect=pygame.Rect(self.x,self.y,self.widht,self.height)
        else:
            rect=self.rect_chosen
        
        mouse_rect = mouse_location()   

        if rect.colliderect(mouse_rect):
            if self.text_movingbar and self.text_movingbar_x < self.lenght:
                self.timer_1 = pygame.time.get_ticks()
                self.text_movingbar = False
            
            if self.timer_2 - self.timer_1 > 0.01  and not self.text_movingbar:
                self.text_movingbar = True
                self.text_movingbar_x += 8
        elif self.rect_chosen !=None:
            self.text_movingbar_x=0
        else:
            if self.text_movingbar and self.text_movingbar_x > 0:
                self.timer_1 = pygame.time.get_ticks()
                self.text_movingbar = False
                
            if self.timer_2 - self.timer_1 > 0.01 and not self.text_movingbar and self.text_movingbar_x>0:
                self.text_movingbar = True
                self.text_movingbar_x -= 8

        pygame.draw.rect(screen,'white',pygame.Rect(self.x-self.lenght/2,self.y+self.y_offset,self.text_movingbar_x,5),border_radius=5)        

class button():
    def __init__(self,text,text_size,x_position,y_position,inner_color,frame_color,text_color):
        self.text = text
        self.text_size = text_size
        self.x_position = x_position
        self.y_position = y_position
        self.inner_color = inner_color
        self.frame_color = frame_color
        self.text_color = text_color
        self.new_size = text_size
        self.new_frame_color = frame_color
        self.button_frame = pygame.Rect(0,0,0,0)
        self.text_width = 0
    def draw_button(self): 
        text_font = pygame.font.SysFont('courier',self.text_size)
        text_shown = text_font.render(self.text, True, self.text_color)
        text_width = text_shown.get_width()
        self.text_width=text_shown.get_width()
        text_height = text_shown.get_height()
        inner_button = pygame.Rect(self.x_position-text_width/2-5,self.y_position-text_height/2-5,10+text_width,10+text_height)
        self.button_frame= pygame.Rect(self.x_position-text_width/2-10,self.y_position-text_height/2-10,20+text_width,20+text_height)
        pygame.draw.rect(screen,self.inner_color,inner_button,border_radius=25)
        pygame.draw.rect(screen,self.frame_color,self.button_frame,5,border_radius=30)
        screen.blit(text_shown,(self.x_position-text_width/2,self.y_position-text_height/2))
    def get_button(self):
        return self.button_frame
    def update(self):
        if mouse_location().colliderect(self.button_frame):
            self.frame_color='green'
            self.text_size=self.new_size
            return True
        else:
            self.frame_color=self.new_frame_color
            self.text_size=self.new_size-5
            return False
    def update_aktive(self):
        if mouse_location().colliderect(self.button_frame):
            return True
        else:
            return False



def rosette(n=7/8,radius=90):
    phi_list=np.linspace(0,50*pi*1000,num=5000)
    x = lambda zeta :  radius*cos(n*zeta)*cos(zeta)
    y = lambda gamma :  radius*cos(n*gamma)*sin(gamma)
    coordiantes = []
    for phi in phi_list:
        coordiantes.append((int(x(phi/1000)),int(y(phi/1000))))
    return coordiantes

class firework():
    def __init__(self,n,radius,x_position,y_position):
        self.n=n
        self.radius=radius
        self.radius_increase=0
        self.x_position = x_position
        self.y_position = y_position
        self.timer_1 = 0
        self.timer_2 = 0 
        self.firework_aktive=True
        self.color = 'red'
    def explode(self):
        self.timer_1 = pygame.time.get_ticks()

        if self.firework_aktive:
            self.timer_2=pygame.time.get_ticks()
            self.radius_increase+=20
            self.firework_aktive=False
        if self.radius_increase>= random.randint(400,500):
            self.x_position = random.randint(100,700)
            self.y_position = random.randint(100,700)
            self.color=color_tupels[random.randint(0,len(color_tupels)-1)]
            self.n = random.randint(20,40)/random.randint(20,40)
            while self.n ==1:
                self.n = random.randint(20,40)/random.randint(20,40)
            self.radius_increase=0
        if self.timer_1 - self.timer_2>random.randint(1,20):
            self.firework_aktive=True

        rosette_list = [pygame.Rect(x+self.x_position ,y+self.y_position,1,1) for x,y in rosette(self.n,self.radius+self.radius_increase)]

        for rosette_coordiantes in rosette_list:
            pygame.draw.rect(screen,self.color,rosette_coordiantes)

    
class rainbow():
    def __init__(self):
        self.timer_1 = 0
        self.timer_2 = 0
        self.rainbow_moving = True
        self.color_tupel_index=0
    def draw_rainbow(self):
        self.timer_1 = pygame.time.get_ticks()
        if self.rainbow_moving:
            self.timer_2= pygame.time.get_ticks()
            self.color_tupel_index+=1
            self.rainbow_moving=False
        for snake in snake_list:
            self.color_tupel_index+=1
            if self.color_tupel_index>337:
                self.color_tupel_index=0
            pygame.draw.rect(screen,color_tupels[self.color_tupel_index],snake)
        if self.timer_1-self.timer_2>10:
            self.rainbow_moving=True
    

        

class formation_rects():
    def __init__(self,x_tupel,y_tupel):
        self.color = 'white'
        self.x_tupel =x_tupel
        self.y_tupel =y_tupel
        self.selected = False
        self.hit_counter = 1
    def get_formation_rect(self):
        return pygame.Rect(self.x_tupel*60+215,self.y_tupel*50+25,50,15)
    def draw_formation_rect(self):
        rect = pygame.Rect(self.x_tupel*60+215,self.y_tupel*50+25,50,15)
        if self.selected:
            if self.hit_counter==1:
                self.color='purple'
            if self.hit_counter==2:
                self.color='green'
            if self.hit_counter==3:
                self.color='yellow'
        elif not self.selected:
            self.color='white'
        pygame.draw.rect(screen,self.color,rect)
    def formation_tupel(self):
        return (self.x_tupel,self.y_tupel,self.hit_counter)

class rotating_letter():
    def __init__(self,letter,starting_angle,color,radius):
        self.letter = letter
        self.starting_angle = starting_angle
        self.color = color
        self.radius = radius
        self.font = pygame.font.SysFont('gadugi', 36)
        self.x_position = 450
        self.y_position = 500

    def show_rotating_letter(self):
        letter_x = self.x_position - int(self.radius* sin(2*pi*(text_rotation_angle-self.starting_angle)/360))
        letter_y = self.y_position - int(self.radius* cos(2*pi*(text_rotation_angle-self.starting_angle)/360))

        letter_show = self.font.render(self.letter, True, self.color)

        letter_rect = letter_show.get_rect()
        
        letter_rect.center=(letter_x,letter_y)
        
        letter_rotated = pygame.transform.rotate(letter_show,text_rotation_angle-self.starting_angle)

        letter_rotated_rect = letter_rotated.get_rect(center=letter_rect.center)

        screen.blit(letter_rotated,letter_rotated_rect)


    



class rectangles():
    def __init__(self,x_size,y_size,x_position,y_position,hit_counter,extra_ball=False,extra_speed=False):
        self.x_size = x_size
        self.y_size = y_size
        self.x_position = x_position
        self.y_position = y_position
        self.hit_counter = hit_counter
        self.extra_ball = extra_ball
        self.extra_speed = extra_speed
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
        if self.extra_ball:
            self.extra_speed=False
        if self.y_position<400 and self.extra_ball:
            pygame.draw.circle(screen,'white',(self.x_position+self.x_size/2,self.y_position+self.y_size/2),self.y_size/5)
        if self.extra_speed and not self.extra_ball and self.y_position<300:
            text_font = pygame.font.SysFont('Arial',40)
            text_shown = text_font.render('<<<', True, 'white')
            text_font_width = text_shown.get_width()
            text_font_height = text_shown.get_height()
            screen.blit(text_shown,(self.x_position-text_font_width/2+self.x_size/2,self.y_position-text_font_height/2+self.y_size/2))
            

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
    global points,ballspeed_aktive
    if rect!=floor:
        if rect.hit_counter==1:
            rect_list.remove(rect)  # Entferne das Rechteck aus der Liste
            if rect.extra_ball:
                ball_list_class.append(balls(390,300,10,10,0,700,0,1,screen,random.choice(ball_colors)))
            if rect.extra_speed:
                ballspeed_aktive=True
        else:
            rect_hit_new = rect.hit_counter-1
            new_rect_to_append = rect
            new_rect_to_append.hit_counter = rect_hit_new
            rect_list.remove(rect)
            rect_list.append(new_rect_to_append)
        points+=20

def moving_rect(dt):
    global lives, points, rect_list, ball_list_class,timer_floor_1,change_color_floor, game_state
    for ball in ball_list_class:
        if ball.get_ball().top < 0:
            ball.y_position_ball=0
            ball.y_speed*= -1
        if ball.get_ball().bottom > 710:
            ball_list_class.remove(ball)
            if ball_list_class==[]:
                ball_list_class.append(balls(400,400,10,10,0,ball.y_speed,0,1,screen,random.choice(ball_colors)))
                lives-=1
                floor.x_position=350
                if lives<=0:
                     game_state='game_over'
        elif ball.get_ball().left < 0 or ball.get_ball().right > 800:
            ball.x_speed *= -1
            if ball.get_ball().left<0:
                ball.x_position_ball=0
            if ball.get_ball().right >800:
                ball.x_position_ball=790
        ball.draw_ball(dt)
    hitbox = 5
    for rect in rect_list:
        for ball in ball_list_class:
            if ball.get_ball().colliderect(rect.get_rectangle()):
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
def rotating_letters(name):
    k=0
    name_list = list(name)
    new_list = []
    for i in range(len(name_list)):
        if name_list[i]==' ':
            k+=12
        else:
            new_list.append((name_list[i],k))
            k+=10
    return new_list


pygame.init()
#rainbowrahmen
rainbow_frame = rainbow()
#spacebar für Pause
space_bar = False
#dsplay
screen = pygame.display.set_mode((900, 800))
screen_width = screen.get_width()   
screen_height = screen.get_height()
#clock 
clock = pygame.time.Clock()


#Settingsbutton und Lebensicon
image_settings=pygame.image.load("settings.jpeg")
image_settings=pygame.transform.scale(image_settings, (40, 40))
heart = "heart.gif"
heart_surface = pygame.image.load(heart)
heart_surface = pygame.transform.scale(heart_surface, (30, 20))
# weißer rahmen im game_state=game
frame_set = pygame.Rect(0,0,800,740)
#ball speed ändern 
ball_speed_timer_1=10000

def text(font='courier',font_size=10,text='',color=(255,255,255),x_position=0,y_position=0,centering=True,scale=False,scale_x=100,scale_y=100):
   '''Funktion für einen Text'''
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
    '''Returns the location of the Mouse as a Rect by 1x1 Pixel'''
    mouse_x_pos,mouse_y_pos=pygame.mouse.get_pos()
    return pygame.Rect(mouse_x_pos,mouse_y_pos,1,1)



#scoreboard lesen mit a um beim wiederöffnen nicht überschrieben wird und falls keine file existiert eine erstellt wird
with open('scoreboard.csv', mode='a', newline='') as file:
   writer = csv.writer(file) 


#floor
floor = rectangles(100,10,350,700,0)
#True False liste
true_false_list = [False]*7+[True]*3
#formation
formation_1 = [(3,0),(4,0),(1,1),(2,1),(5,1),(6,1),(0,2),(1,2),(2,2),(5,2),(6,2),(7,2),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3)]
rect_list=[rectangles(90,35,100*i+5,40*j+5,random.randint(1,3),random.choice(true_false_list),random.choice(true_false_list)) for i,j in formation_1 ]
rect_list.append(floor)

#formation list in selected mode
formation_list = [formation_rects(x,y) for x in range(8) for y in range(5)]
seleceted_formation_list=[]
formation_safed=False

#allgemeine Variablen
points=0 #Punkte
timer_floor_1=1 #Farbänderung
change_color_floor=False
lives=3 #Leben 
one_run = 1 #one_run damit der name nur einmal ins Scoreboard gespeichert wird 
name="" 
name_left=True
difficulty_level='easy'
floor_x_speed=600
running = True
moving_text_menu=True
moving_text_game=True
#Für die regenbogen Farbenschrift
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
#gamestate menu anfang
game_state='menu'

text_movingbar=True
text_movingbar_x=0
text_movingbar_x_2=0
color_tupel_index =0
color_tupel_index_start =0
#Rahmenliste der Rechteke
snake_list = [pygame.Rect(i*10,0,10,10) for i in range(90)] + [pygame.Rect(890,10+i*10,10,10) for i in range(79)]+[pygame.Rect(890-i*10,790,10,10) for i in range(89)]+[pygame.Rect(0,790-i*10,10,10) for i in range(79)]

#rotation des Text
text_rotation_aktivated=True
text_rotation_angle=0
radius_aktive=False
radius_increase=0
timer_radius_aktive=True
shrinking_radius=False
color_tupel_index_ring=0
#buttons
menu_button = button('menu',40,150,450,'navy','white','white')
resume_button = button('resume',40,450,450,'navy','white','white')
start_button =  button('start',50,450,500,'navy','white',(255,0,100))
safe_button =  button('safe',50,450,450,'black','white','white')
quit_button =  button('quit',40,750,450,'navy','white','white')
play_again_button = button('play again',40,450,450,'navy','white','white')
easy_button=button('easy',40,150,200,'black','white','white')
easy_moving_bar = moving_bar(150,200,-200,-25,100,20,None)
medium_button=button('medium',40,450,200,'black','white','white')
medium_moving_bar = moving_bar(450,200,-200,-25,100,20,None)   
hard_button=button('hard',40,750,200,'black','white','white')
hard_moving_bar = moving_bar(750,200,-200,-25,100,20,None)
reset_button=button('reset scoreboard',40,450,450,'black','white','white')
reset_moving_bar = moving_bar(450,450,-200,-25,100,20,None)
select_button=button('select formation',40,450,550,'black','white','white')
selectet_moving_bar = moving_bar(450,550,-200,-25,100,20,None)
#rest 
reset_game=False
#rosette    
rosette_angle=0
rosette_rotating_aktive=True
radius_change=90
change_sign = 1
rosette_look = 7/8
rosetten_color='white'
i_rosette=0
#firework
firework_1=firework(7/8,0,100,100)
firework_2=firework(3/8,0,400,800)
firework_3=firework(1/8,0,300,300)
#Auswahl für den Hit counter 
chosen_hit_counter=1
butten_1_hit=button('1 Hits',30,250,300,'purple','black','black')
butten_2_hit=button('2 Hits',30,450,300,'green','black','black')
butten_3_hit=button('3 Hits',30,650,300,'yellow','black','black')
#loosing ring
lose_ring = [rotating_letter(letter_chose,angle,'white',100) for letter_chose,angle in [('Y',0),('o',10),('u',20),(' ',30),('L',40),('o',50),('s',60),('e',70),('Y',90),('o',100),('u',110),(' ',120),('L',130),('o',140),('s',150),('e',160),('Y',180),('o',190),('u',200),(' ',210),('L',220),('o',230),('s',240),('e',250),('Y',260),('o',270),('u',280),(' ',290),('L',300),('o',310),('s',320),('e',330)]]
ring_moving_aktive=True
alpha=0
butterfly=rosette(n=1/2,radius=300)
#ballspeed 
ballspeed_aktive=False
dt = 0.005
ball_speed_reset=False
while running:
    
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
                rect_list = [rectangles(90,35,i*100+5,j*40+5,random.randint(1,3),True) for i in range(8) for j in range(5)]
                rect_list.append(floor)
                floor.x_position=350
                points=0
                lives=4
                game_state='game'
           
        
        if event.type == pygame.MOUSEBUTTONDOWN and (game_state=='game_over' or game_state=='game_won'):
            if mouse_location().colliderect(play_again_button.get_button()):
                reset_game=True
                game_state='game'
            if mouse_location().colliderect(menu_button.get_button()):
                reset_game=True
                game_state='menu'
        if event.type == pygame.MOUSEBUTTONDOWN and game_state=='menu':
            if mouse_location().colliderect(pygame.Rect(10,750,40,40)):
                game_state='menu+settings'
            if mouse_location().colliderect(start_button.get_button()) and not name_left:
                shrinking_radius=True

        if event.type == pygame.MOUSEBUTTONDOWN and game_state=='pause':
            if mouse_location().colliderect(resume_button.get_button()):
                game_state='game'
            if mouse_location().colliderect(menu_button.get_button()):
                game_state='menu'
                radius_increase=0
                shrinking_radius=False


        if event.type == pygame.MOUSEBUTTONDOWN and game_state=='menu+settings':
            if mouse_location().colliderect(pygame.Rect(730,745,100,30)):
                game_state='menu'
            if mouse_location().colliderect(easy_button.get_button()):
                difficulty_level='easy'
            if mouse_location().colliderect(medium_button.get_button()):
                difficulty_level='medium'
            if mouse_location().colliderect(hard_button.get_button()):
                difficulty_level='hard'
            if mouse_location().colliderect(select_button.get_button()):
                game_state='menu+settings+formation'
        if event.type == pygame.MOUSEBUTTONUP and game_state=='menu+settings':
             if mouse_location().colliderect(reset_button.get_button()):
                with open('scoreboard.csv', mode='w', newline='') as file:
                    writer = csv.writer(file) 

        if event.type == pygame.MOUSEBUTTONUP and game_state=='menu+settings+formation':
            if mouse_location().colliderect(pygame.Rect(730,745,100,30)):
                game_state='menu+settings'
            if mouse_location().colliderect(butten_1_hit.get_button()):
                chosen_hit_counter=1
            if mouse_location().colliderect(butten_2_hit.get_button()):
                chosen_hit_counter=2
            if mouse_location().colliderect(butten_3_hit.get_button()):
                chosen_hit_counter=3
            for formation_rect in formation_list:
                if mouse_location().colliderect(formation_rect.get_formation_rect()) and not formation_rect.selected and formation_rect.formation_tupel() not in seleceted_formation_list:
                    formation_rect.selected=True
                    formation_rect.hit_counter=chosen_hit_counter
                    seleceted_formation_list.append(formation_rect.formation_tupel())
                elif mouse_location().colliderect(formation_rect.get_formation_rect()) and formation_rect.selected and formation_rect.formation_tupel() in seleceted_formation_list:
                    formation_rect.selected=False
                    seleceted_formation_list.remove(formation_rect.formation_tupel())
            if mouse_location().colliderect(safe_button.get_button()) and not formation_safed and seleceted_formation_list!=[]:
                formation_safed=True
            elif mouse_location().colliderect(safe_button.get_button()) and formation_safed:
                formation_safed=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_location().colliderect(quit_button.get_button()) and quit_button.update_aktive():
                running =False


    
    if reset_game:
        reset_game=False
        ball_1 =  balls(390,300,10,10,0,700,0,1,screen,random.choice(ball_colors))
        ball_list_class = [ball_1]
        rect_list = [rectangles(90,35,i*100+5,j*40+5,random.randint(1,3),random.choice(true_false_list),random.choice(true_false_list)) for i in range(8) for j in range(5)]
        rect_list.append(floor)
        floor.x_position=350
        points=0
        lives=4
        radius_increase=0
        shrinking_radius=False


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
    
    
    if lives >0 and rect_list==[floor]:
        game_state='game_won'   

    if formation_safed and seleceted_formation_list!=[] and game_state=='menu+settings+formation':     
        rect_list=[rectangles(90,35,100*i+5,40*j+5,k) for i,j,k in seleceted_formation_list]
        rect_list.append(floor)


    if game_state=='menu':
        dt = 0.005
        screen.fill("black")
        
        timer_rosette_1 = pygame.time.get_ticks()

        if rosette_rotating_aktive:
            timer_rosette_2 = pygame.time.get_ticks()
            rosette_angle+=1
            radius_change-=1*change_sign
            i_rosette+=1
            if i_rosette >= len(color_tupels):
                i_rosette=0
            rosetten_color=color_tupels[i_rosette]
            if radius_change<0:
                change_sign=-1
                rosette_look = random.randint(1,20)/random.randint(1,20)
                while rosette_look==1:
                    rosette_look = random.randint(1,20)/random.randint(1,20)
            if radius_change>90:
                change_sign=1
            rosette_rotating_aktive=False
        
        if timer_rosette_1- timer_rosette_2> 10:
            rosette_rotating_aktive=True
        
        
        
        rosette_list = [pygame.Rect(int(x*cos(rosette_angle/100)-y*sin(rosette_angle/100))+450,int(x*sin(rosette_angle/100)+y*cos(rosette_angle/100))+500,1,1) for x,y in rosette(n=rosette_look,radius=radius_change)]

        for rosette_coordiantes in rosette_list:
            pygame.draw.rect(screen,rosetten_color,rosette_coordiantes)
    
        
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

        

    
        letter_ring = [rotating_letter(letter_chose,angle,'white',100) for letter_chose,angle in [('W', 0), ('e', 10), ('l', 20), ('c', 30), ('o', 40), ('m', 50), ('e', 60), ('t',72), ('o',78),('B', 90), ('r', 100), ('e', 110), ('a', 120), ('k', 130), ('o', 140), ('u', 150), ('t', 160),('W', 180), ('e', 190), ('l', 200), ('c', 210), ('o', 220), ('m', 230), ('e', 240),('t',252),('o',258),('B', 270), ('r', 280), ('e', 290), ('a', 300), ('k', 310), ('o', 320), ('u', 330), ('t', 340)]]
        
        timer_radius_1=pygame.time.get_ticks()
        for letters in letter_ring:
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
        


        text_rotation_timer_1 = pygame.time.get_ticks()
        if text_rotation_aktivated:
            text_rotation_timer_2=pygame.time.get_ticks()
            text_rotation_aktivated=False
            text_rotation_angle+=1
        if text_rotation_timer_1-text_rotation_timer_2>2:
            text_rotation_aktivated=True
       
        timer_1 = pygame.time.get_ticks()
        text(font='courier',font_size=50,text='Welcome to Breakout',x_position=450+x_text_moving_menu,y_position=60,color=(color_red,color_green,color_blue))
        text(font='courier',font_size=50,text='Welcome to Breakout',x_position=-450+x_text_moving_menu,y_position=60,color=(color_red,color_green,color_blue))
        
        
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
        if name.strip()=='':
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
        
        if name.strip()=='' or shrinking_radius:
            pass
        else:
            if ball_list_class[0].y_position_ball==300:
                start_button.text='start'
            else:
                start_button.text='resume'
            start_button.draw_button()
            if start_button.update_aktive() and not shrinking_radius:   
                radius_aktive=True
            elif not start_button.update_aktive() and not shrinking_radius:
                radius_aktive=False
            start_button.update()

        
        
        screen.blit(image_settings,(30-x/2,770-y/2))

        rainbow_frame.draw_rainbow()

    
    if game_state=='menu+settings':
        screen.fill("black")

        
        button('Settings',50,450,60,'black','white','white').draw_button()

        if mouse_location().colliderect(pygame.Rect(730,745,100,30)):
            text(font_size=40,text='menu',x_position=780,y_position=760)
        else:
            text(font_size=30,text='menu',x_position=780,y_position=760)        

        
        easy_button.draw_button()
        easy_button.update()
        if easy_button.update_aktive() or difficulty_level=='easy':
            easy_button.text_color=(255,0,100)
            easy_button.frame_color='white'
            if easy_button.update_aktive() or not difficulty_level=='easy':
                easy_button.frame_color='black'
        else:
            easy_button.text_color='white'
        easy_moving_bar.lenght=easy_button.text_width
        easy_moving_bar.rect_chosen=easy_button.get_button()
        easy_moving_bar.update()


        medium_button.draw_button()
        medium_button.update()
        if medium_button.update_aktive() or difficulty_level=='medium':
            medium_button.text_color=(255,0,100)
            medium_button.frame_color='white'
            if medium_button.update_aktive() or not difficulty_level=='medium':
                medium_button.frame_color='black'
        else:
            medium_button.text_color='white'
        medium_moving_bar.lenght=medium_button.text_width
        medium_moving_bar.rect_chosen=medium_button.get_button()
        medium_moving_bar.update()
        

        hard_button.draw_button()
        hard_button.update()
        if hard_button.update_aktive() or difficulty_level=='hard':
            hard_button.text_color=(255,0,100)
            hard_button.frame_color='white'
            if hard_button.update_aktive() or not difficulty_level=='hard':
                hard_button.frame_color='black'
        else:
            hard_button.text_color='white'
        hard_moving_bar.lenght=hard_button.text_width
        hard_moving_bar.rect_chosen=hard_button.get_button()
        hard_moving_bar.update()

        select_button.draw_button()
        select_button.update()
        if select_button.update_aktive():
           select_button.text_color=(255,0,100)
           select_button.frame_color='black'
        else:
           select_button.text_color='white'
        selectet_moving_bar.lenght=select_button.text_width
        selectet_moving_bar.rect_chosen=select_button.get_button()
        selectet_moving_bar.update()


        reset_button.draw_button()
        reset_button.update()
        if reset_button.update_aktive():
            reset_button.text_color=(255,0,100)
            reset_button.frame_color='black'
        else:
            reset_button.text_color='white'
        reset_moving_bar.lenght=reset_button.text_width
        reset_moving_bar.rect_chosen=reset_button.get_button()
        reset_moving_bar.update()

        if mouse_location().colliderect(easy_button.get_button()):
            text(font_size=30,text='floorsize = 100 px and floorspeed = 600',x_position=450,y_position=300,centering=True,color=(255,0,100))
        
        if mouse_location().colliderect(medium_button.get_button()):
            text(font_size=30,text='floorsize = 50 px and floorspeed = 500',x_position=450,y_position=300,centering=True,color=(255,0,100))
       
        if mouse_location().colliderect(hard_button.get_button()):
            text(font_size=30,text='floorsize = 25 px and floorspeed = 400',x_position=450,y_position=300,centering=True,color=(255,0,100))
        
        rainbow_frame.draw_rainbow()
    
    if game_state=='menu+settings+formation':
        screen.fill("black")
        if mouse_location().colliderect(pygame.Rect(730,745,100,30)):
            text(font_size=40,text='back',x_position=780,y_position=760)
        else:
            text(font_size=30,text='back',x_position=780,y_position=760)
        
        [formation_list[i].draw_formation_rect() for i in range(len(formation_list))]
        if formation_safed and seleceted_formation_list!=[]:
            safe_button.text_color=(255,0,200)
            safe_button.text='safed'
        else:
            safe_button.text='safe'
            safe_button.text_color='white'
            

        safe_button.update()
        
        safe_button.draw_button()
        

        butten_1_hit.draw_button()
        butten_1_hit.update()
        butten_2_hit.draw_button()
        butten_2_hit.update()
        butten_3_hit.draw_button()
        butten_3_hit.update()

        if chosen_hit_counter==1:
            butten_1_hit.text_color='red'
        else:
            butten_1_hit.text_color='black'

        if chosen_hit_counter==2:
            butten_2_hit.text_color='red'
        else:
            butten_2_hit.text_color='black'
        
        if chosen_hit_counter==3:
            butten_3_hit.text_color='red'
        else:
            butten_3_hit.text_color='black'


        if safe_button.update_aktive() and seleceted_formation_list==[]:
            no_formation_text = button('no formation selected',30,450,550,'black','black','white')
            no_formation_text.draw_button()

        rainbow_frame.draw_rainbow()

    if game_state=='game':      
        screen.fill("black")
        pygame.draw.rect(screen,"white",frame_set,5)
        
        if pressed_keys[pygame.K_a] and floor.get_rectangle().left > 0:
            floor.x_position  -= floor_x_speed * dt
        if floor.get_rectangle().left<0:
                 floor.x_position=0
        if pressed_keys[pygame.K_d] and floor.get_rectangle().right < 800:
            floor.x_position += floor_x_speed * dt
        if floor.get_rectangle().right>800:
                floor.x_position=800-floor.x_size
        for brick in rect_list:
             brick.draw_rectangles()

        timer_floor_2 = pygame.time.get_ticks()

        #game interaktion
        moving_rect(dt)


        if change_color_floor==True:
             floor.hit_counter=1
        if timer_floor_2-timer_floor_1>200:
             change_color_floor=False
             floor.hit_counter=0


        if ballspeed_aktive:
            ballspeed_aktive=False
            ball_speed_reset=True
            ball_speed_timer_1=pygame.time.get_ticks()
            dt=0.007
            for ball in ball_list_class:
                ball.x_speed*=1.1
                ball.y_speed*=1.1
        
        ball_speed_timer_2 = pygame.time.get_ticks()
        if ball_speed_timer_2-ball_speed_timer_1>1000:
            dt=0.005
            if ball_speed_reset:
                ball_speed_reset=False
                for ball in ball_list_class:
                    ball.x_speed*=1/1.1
                    ball.y_speed*=1/1.1


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
        text(font='courier',font_size=30,text='press spacebar to pause game or esc to quit',x_position=450+x_text_moving_game,y_position=775)
        text(font='courier',font_size=30,text='press spacebar to pause game or esc to quit',x_position=-450+x_text_moving_game,y_position=775)
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
        
        
        menu_button.update()
        menu_button.draw_button()

        play_again_button.draw_button()
        play_again_button.update()
        quit_button.draw_button()
        quit_button.update()

        if lives==0:
            with open('scoreboard.csv', mode='a', newline='') as file:
                            writer = csv.writer(file) 
                            writer.writerow([name.strip(),points])
        lives=-1
        timer_loosing= pygame.time.get_ticks()
        text(font='courier',font_size=30,text='You Lose'+' '*20+'You Lose',x_position=450+x_text_moving_loosing,y_position=775)
        text(font='courier',font_size=30,text='You Lose'+' '*20+'You Lose',x_position=-450+x_text_moving_loosing,y_position=775)
        text(font='courier',font_size=30,text='You Lose'+' '*20+'You Lose',x_position=450+x_text_moving_loosing,y_position=25)
        text(font='courier',font_size=30,text='You Lose'+' '*20+'You Lose',x_position=-450+x_text_moving_loosing,y_position=25)
        if moving_text_loosing == True:
            timer_loosing_2 = pygame.time.get_ticks()
            moving_text_loosing=False
            x_text_moving_loosing+=3
        if timer_loosing- timer_loosing_2 >=5:
             moving_text_loosing=True
        if x_text_moving_loosing>900:
             x_text_moving_loosing=-1


        rainbow_frame.draw_rainbow()

    if game_state=='game_won':
        screen.fill('Black')

        button('Points: '+str(points),40,450,100,'black','black','white').draw_button()
        firework_1.explode()
        firework_2.explode()
        firework_3.explode()
        
        menu_button.draw_button()
        menu_button.update()
        quit_button.draw_button()
        quit_button.update()
        play_again_button.draw_button()
        play_again_button.update()

        if one_run==1:
            with open('scoreboard.csv', mode='a', newline='') as file:
                            writer = csv.writer(file) 
                            writer.writerow([name.strip(),points])
        
        one_run+=1
        rainbow_frame.draw_rainbow()
    
        
    

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


        button('Points: '+str(points),40,450,100,'navy','white','white').draw_button()
       

        # menu butten
       
       
        quit_button.draw_button()
        quit_button.update()
        menu_button.draw_button()
        resume_button.draw_button()
        menu_button.update()
        resume_button.update()
        
        lose_rings = [rotating_letter(letter_chose,angle,'white',100) for letter_chose,angle in rotating_letters('Pause '*6)]
        welcom_ring = [rotating_letter(letter_chose,angle,'white',100) for letter_chose,angle in rotating_letters('Breakout '*4)]

        
        timer_ring_1 = pygame.time.get_ticks()
        if ring_moving_aktive: 
            ring_moving_aktive=False
            alpha+=1
            if alpha>=len(rosette(n=3)):
                alpha=0
            timer_ring_2 = pygame.time.get_ticks()
        
        if timer_ring_1-timer_ring_2>30:
            ring_moving_aktive=True
        

        for letters in lose_rings:
            letters.x_position=450+300*cos(alpha/100)
            letters.y_position=450+300*sin(alpha/100)
            letters.show_rotating_letter()


        for letters in welcom_ring:
            letters.x_position=450+butterfly[alpha][0]
            letters.y_position=450+butterfly[alpha][1]
            letters.show_rotating_letter()
        
        text_rotation_timer_1 = pygame.time.get_ticks()
        if text_rotation_aktivated:
            text_rotation_timer_2=pygame.time.get_ticks()
            text_rotation_aktivated=False
            text_rotation_angle+=1
        if text_rotation_timer_1-text_rotation_timer_2>2:
            text_rotation_aktivated=True
        rainbow_frame.draw_rainbow()
    clock.tick(120)
    pygame.display.flip()
pygame.quit()