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
    def __init__(self, x_position_ball, y_position_ball, x_size, y_size, x_speed,y_speed,dx,dy,surface):
        self.x_size = x_size
        self.y_size = y_size 
        self.x_position_ball = x_position_ball
        self.y_position_ball = y_position_ball
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.dx = dx
        self.dy = dy
        self.surface = surface
    def draw_ball(self,dt):
        self.y_position_ball += self.y_speed * dt * self.dy
        self.x_position_ball += self.x_speed * dt * self.dx
        ball_rect = pygame.Rect(self.x_position_ball, self.y_position_ball, self.x_size, self.y_size)
        pygame.draw.rect(self.surface, "red", ball_rect)
    def get_ball(self):
        return pygame.Rect(self.x_position_ball, self.y_position_ball, self.x_size, self.y_size)
        
    


def moving_rect(dt):
    global lives, points, rect_test_list, ball_list_class,game_over,timer_floor_1,change_color_floor
    for ball in ball_list_class:
        if ball.get_ball().top < 0:
            ball.y_speed*= -1
        if ball.get_ball().bottom > 800:
            ball_list_class.remove(ball)
            if ball_list_class==[]:
                ball_list_class.append(balls(400,400,10,10,0,400,0,1,screen))
                lives-=1
                if lives<=0:
                     game_over=True
        elif ball.get_ball().left < 0 or ball.get_ball().right > 800:
            ball.x_speed *= -1
            if ball.get_ball().left<0:
                ball.x_position_ball=0
            if ball.get_ball().right >800:
                ball.x_position_ball=790
        ball.draw_ball(dt)
    hitbox = 5
    for rect in rect_test_list:
        for ball in ball_list_class:
            if ball.get_ball().colliderect(rect.get_rectangle()):
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
                if rect==floor:
                    timer_floor_1 = pygame.time.get_ticks()
                    change_color_floor=True
                    if ball.x_speed==0:
                        ball.x_speed=400*random.choice([-1,1])
                    ball.dy = random.randint(5,9)/10
                    ball.dx = round(sqrt(1-ball.dy**2),6)
                    ball.y_position_ball=floor.y_position-ball.y_size
                if abs(ball.get_ball().bottom - rect.get_rectangle().top) < hitbox and ball.y_speed > 0:
                    ball.y_position_ball=rect.get_rectangle().top-ball.y_size
                    ball.y_speed *= -1
                elif abs(ball.get_ball().top - rect.get_rectangle().bottom) < hitbox and ball.y_speed < 0:
                    ball.y_position_ball=rect.get_rectangle().bottom
                    ball.y_speed *= -1
                elif abs(ball.get_ball().left - rect.get_rectangle().right) < hitbox and ball.x_speed < 0:
                    ball.x_position_ball=rect.get_rectangle().right
                    ball.x_speed *= -1
                elif abs(ball.get_ball().right - rect.get_rectangle().left) < hitbox and ball.x_speed > 0:
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
heart = "heart.gif"
heart_surface = pygame.image.load(heart)
heart_surface = pygame.transform.scale(heart_surface, (30, 20))
image_width = image.get_width()
image_height = image.get_height()
image_x = (screen_width - image_width) // 2  
image_y = (screen_height - image_height) // 2
frame_set = pygame.Rect(0,0,800,740)

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


losing_list = []
for i in range(1,10):
            losing_list.append(text_1)

#scoreboard 

with open('scoreboard.csv', mode='a', newline='') as file:
   writer = csv.writer(file) 

#rechtecke
floor = rectangles(100,10,350,700,0)
rect_test_list = [rectangles(90,20,i*100+5,j*25+5,random.randint(1,3)) for i in range(8) for j in range(4)]
rect_test_list.append(floor)


points=0
timer_floor_1=1
lives=3
one_run = 1 
name=""
running = True
reset_game=False
menu = True
moving_text_menu=True
moving_text_game=True
change_color_floor=False
x,y,z=230,230,230
x_text_moving_menu=0
x_text_moving_game=0
reset_pressed=False
game_over = False
#Bälle
ball_1 =  balls(390,300,10,10,0,400,0,1,screen)
ball_2 =  balls(390,200,10,10,0,400,0,1,screen)
ball_3 =  balls(390,200,10,10,300,300,0.6,0.8,screen)
ball_list_class = [ball_1,ball_2]



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
            if event.key == pygame.K_t and game_over and lives<=0:
                ball_list_class = [ball_1,ball_2]
                rect_test_list = [rectangles(90,20,i*100+5,j*25+5,random.randint(1,3)) for i in range(8) for j in range(4)]
                rect_test_list.append(floor)
                floor.x_position=350
                points=0
                lives=4
                game_over=True

    if menu:
        dt = clock.tick(120)/1000
        screen.fill("black")
        if ball_3.x_position_ball >900 or ball_3.x_position_ball<0:
            ball_3.x_speed*=-1
        if ball_3.y_position_ball >800 or ball_3.y_position_ball<0:
            ball_3.y_speed*=-1
        ball_3.draw_ball(dt)

        timer_1 = pygame.time.get_ticks()
        if x<=20 or x>=255:
             x=230
        if y<=20 or y>=255:
             y=230
        if z<=20 or z>=255:
             z=230 
        text(font='Arial',font_size=50,text='Welcome to Breakout',x_position=450+x_text_moving_menu,y_position=60,color=(x,y,z))
        text(font='Arial',font_size=50,text='Welcome to Breakout',x_position=-450+x_text_moving_menu,y_position=60,color=(x,y,z))
        if moving_text_menu == True:
            timer_2 = pygame.time.get_ticks()
            moving_text_menu=False
            x=x+random.randint(-4,1)
            y=y+random.randint(-1,4)
            z=z+random.randint(-4,1)
            x_text_moving_menu+=3
        if timer_1 - timer_2 >=5:
             moving_text_menu=True
        if x_text_moving_menu>900:
             x_text_moving_menu=-1

        text(font_size=50,text='name: '+name,x_position=300,y_position=300,centering=False)
        clock.tick(120)
        pygame.display.flip()

    if lives>0 and rect_test_list!=[floor] and not space_bar and not menu or reset_pressed:        
        screen.fill("black")
        pygame.draw.rect(screen,"white",frame_set,5)
        dt = clock.tick(120) / 1000
        if pressed_keys[pygame.K_a] and floor.get_rectangle().left > 0:
            floor.x_position  -= 600 * dt
        if floor.get_rectangle().left<0:
                 floor.x_position=0
        if pressed_keys[pygame.K_d] and floor.get_rectangle().right < 800:
            floor.x_position += 600 * dt
        if floor.get_rectangle().right>800:
                floor.x_position=700
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
        pygame.display.flip()
        clock.tick(120)

    if lives<=0 and game_over:
        screen.fill("Black")
        screen.blit(text_1,(text_1_x,text_1_y))
        text(font_size=50,text='press t to play again or q to quit',x_position=450,y_position=500)
        for text_1_1 in losing_list:
            random.randint(0,800)
            screen.blit(text_1_1,(random.randint(0,800),random.randint(0,800)))
        if lives==0:
            with open('scoreboard.csv', mode='a', newline='') as file:
                            writer = csv.writer(file) 
                            writer.writerow([str(name),points])
        lives=-1
        
        clock.tick(120)
        pygame.display.flip()
    if rect_test_list == [floor] and lives >0:
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
        text(font_size=30,text='Points: '+str(points),x_position=450,y_position=400)
        text(font_size=30,text='press c to continue or esc for quit',x_position=450,y_position=450)
        clock.tick(120)
        pygame.display.flip()
    
pygame.quit()
