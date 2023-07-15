import pygame
import random

pygame.init()

#variables

squares_height = 20             #has to be even
squares_width = 10              #has to be even
square = 30
screen_x = squares_width*square
screen_y = squares_height*square

squares_height_multi = 20       #has to be even
squares_width_multi = 21        #has to be divisable by three
square_multi = 30             
screen_x_multi = squares_width_multi*square_multi 
screen_y_multi = squares_height_multi*square_multi
game_state ='menu'

screen_sizes = {
    'menu': (screen_x_multi, screen_y_multi),
    'single': (screen_x, screen_y),
    'multi': (screen_x_multi, screen_y_multi)
}

current_screen_size = screen_sizes['single']

screen = pygame.display.set_mode(current_screen_size)

x_offset, x_offset_1, x_offset_2 = 0,0,0
y_offset, y_offset_1, y_offset_2 = 0,0,0
running = True
screen = pygame.display.set_mode((screen_x,screen_y))
clock = pygame.time.Clock()
tets=random.randint(0,6)                                 #list of rects of current tetromino (index from the move() function for the sublist including the positions of the rects for one tetromino)
tets1=random.randint(0,6)
tets2=random.randint(0,6)
rects=0
stop_time=0
single_player_activated = True #Default 

#list of the landed tetrominos
landed_tetrominos = []
colours_landed = []

#grid squares for the whole screen
grid_squares = [pygame.Rect(i*square,j*square,square,square) for i in range(squares_width) for j in range(squares_height)]
grid_squares_multi = [pygame.Rect(i*square_multi,j*square_multi,square_multi,square_multi) for i in range(squares_width_multi) for j in range(squares_height_multi)]

#tetrominos
tetrominos_positions = [
    [(-1, 0), (0, 0), (1, 0), (2, 0)],  #I
    [(1, 0), (-1, 1), (0, 1), (1, 1)],  #L1
    [(1, 1), (-1, 0), (0, 0), (1, 0)],  #L2
    [(-1, 0), (0, 0), (-1, 1), (0, 1)], #O
    [(0, 0), (1, 0), (-1, 1), (0, 1)],  #S1
    [(1, 0), (0, 0), (2, 1), (1, 1)],   #S2
    [(0, 0), (-1, 1), (0, 1), (1, 1)],  #T
]

tetrominos_positions_2 = [
    [(-2, 0), (-1, 0), (0, 0), (1, 0)],  #I
    [(1, 0), (-1, 1), (0, 1), (1, 1)],  #L1
    [(1, 1), (-1, 0), (0, 0), (1, 0)],  #L2
    [(-1, 0), (0, 0), (-1, 1), (0, 1)], #O
    [(0, 0), (1, 0), (-1, 1), (0, 1)],  #S1
    [(0, 0), (-1, 0), (1, 1), (0, 1)],   #S2
    [(0, 0), (-1, 1), (0, 1), (1, 1)],  #T
]

tetromino_colors = {
    0: (255, 0, 0),     #red for I
    1: (0, 255, 0),     #green for L1
    2: (0, 0, 255),     #blue for L2
    3: (255, 255, 0),   #yellow for O
    4: (255, 0, 255),   #pink for S2
    5: (148, 71, 230),  #purple for S2
    6: (52, 235, 235),  #turqouise for T
}


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
    def draw_button(self): 
        text_font = pygame.font.SysFont('arial',self.text_size)
        text_shown = text_font.render(self.text, True, self.text_color)
        text_width = text_shown.get_width()
        text_height = text_shown.get_height()
        inner_button = pygame.Rect(self.x_position-text_width/2-5,self.y_position-text_height/2-5,10+text_width,10+text_height)
        self.button_frame= pygame.Rect(self.x_position-text_width/2-10,self.y_position-text_height/2-10,20+text_width,20+text_height)
        pygame.draw.rect(screen,self.inner_color,inner_button,border_radius=25)
        pygame.draw.rect(screen,self.frame_color,self.button_frame,3,border_radius=30)
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
        

welcome_button = button('Welcome to Tetris!', 30, screen_x/2, 3*square, 'black', 'black', 'white')    
pause_button = button('PAUSE - press \'c\' to continue ', 25 , screen_x/2, screen_y/2, 'black', 'black', 'white')    
singleplayer_button = button('Singleplayer', 20, screen_x/3, screen_y/3+2*square, 'black','white', 'white')
multiplayer_button = button('Multiplayer', 20, 2*screen_x/3, screen_y/3+2*square, 'black', 'white','white')
start_button = button('START', 30, screen_x/2, 2*screen_y/3, 'navy', 'white', (255,0,200))
lose_button = button('YOU LOSE! - press \'m\' to go back to the menu', 15, screen_x/2, screen_y/2, 'black', 'black', 'white')

#functions
def draw_grid(grid_squares):
    '''
    drawing the grid
    '''
    [pygame.draw.rect(screen,(78,78,78), grid_rects, 1) for grid_rects in grid_squares]             # drawing grid from grid_square list

def move(y_offset,x_offset,square,screen_x,tetrominos_positions,start='middle'):     
    '''
    moves rects vertical per keydown and with constant speed downwards
    '''
    if start=='middle':
        start_position = 2
    if start=='left':
        start_position = 3
    if start=='right':
        start_position =3/2

    return [[pygame.Rect(x*square+screen_x/start_position-square+x_offset,y*square+y_offset,square,square) for x,y in tetrect_pos] for tetrect_pos in tetrominos_positions]

def collide_right(moving_tetromino,screen_x, square= square):
    '''
    returns bool about whether the current tetromino collides with the left border
    '''
    for rect in moving_tetromino:
        collision_rect = rect.copy()
        collision_rect.x -= square
        if collision_rect.x >= screen_x - 2*square:
            return True  #collision with left border
    return False  #no collision with left border

def collide_left(moving_tetromino, square = square):
    '''
    returns bool about whether the current tetromino collides with the left border
    '''
    for rect in moving_tetromino:
        collision_rect = rect.copy()
        collision_rect.x += square
        if collision_rect.x <= 0 + square:
            return True  #collision with right border
    return False  #no collision with right border

def collide_landed(moving_tetromino, square = square):
    '''
    returns bool about whether the current tetromino collides with another tetromino that already landed
    (rects relate to the points in the upper left corner, so we have to check whether the tetromino will touch the ground in the next step)
    '''
    global running, game_state, landed_tetrominos, colours_landed #important because the variables in functions are only local if we don't set them global
    for rect in moving_tetromino:
        collision_rect = rect.copy()  #create copy of the rect
        collision_rect.y += square  #move rect one square down
        for list in landed_tetrominos:
            if collision_rect.collidelist(list) != -1 and not rect.y == 0:
                #collidelist returns index of the first colliding figure and -1 if theres no collision
                return True  #no collision with tetromino that has already landed in the next square
            elif collision_rect.collidelist(list) != -1 and rect.y == 0:
                landed_tetrominos = []
                colours_landed = []
                game_state = 'lose'   
    return False  #collision with tetromino that has already landed in the next square

def collide_ground(moving_tetromino, screen_y = screen_y):
    '''
    returns bool about whether the current tetromino touches the ground
    '''
    for rect in moving_tetromino:
        if rect.bottom==screen_y:
            return True
    return False

def collide_landed_left(moving_tetromino, square = square):
    global running,game_state
    for rect in moving_tetromino:
        collision_rect = rect.copy()  #create copy of the rect
        collision_rect.x -= square
        for list in landed_tetrominos:
            if collision_rect.collidelist(list)!=-1 and not rect.y == 0:
                #collidelist returns index of the first colliding figure and -1 if theres no collision
                return True  #no collision with tetromino that has already landed in the next square
            elif collision_rect.collidelist(list)!=-1 and rect.y == 0:
                game_state = 'lose'   
    return False

def collide_landed_right(moving_tetromino, square = square):
    global running,game_state
    for rect in moving_tetromino:
        collision_rect = rect.copy()  #create copy of the rectfpr
        collision_rect.x += square
        for list in landed_tetrominos:
            if collision_rect.collidelist(list)!=-1 and not rect.y == 0:
                #collidelist returns index of the first colliding figure and -1 if theres no collision
                return True  #no collision with tetromino that has already landed in the next square
            elif collision_rect.collidelist(list)!=-1 and rect.y == 0:
                game_state = 'lose'   
    return False

def moving_collide_left():
    global running, landed_tetrominos
    for rect in moving_tetromino_1: 
        collision_rect = rect.copy()  #create copy of the rect
        collision_rect.x += square_multi
        if collision_rect.collidelist(moving_tetromino_2)!=-1 and not rect.y == 0:
            #collidelist returns index of the first colliding figure and -1 if theres no collision
            return True  #no collision with tetromino that has already landed in the next square
        elif collision_rect.collidelist(moving_tetromino_2)!=-1 and rect.y == 0:
            running = False    
    return False  #collision with tetromino that has already landed in the next square

def moving_collide_right():
    global running, landed_tetrominos
    for rect in moving_tetromino_1: 
        collision_rect = rect.copy()  #create copy of the rect
        collision_rect.x -= square_multi
        if collision_rect.collidelist(moving_tetromino_2)!=-1 and not rect.y == 0:
            #collidelist returns index of the first colliding figure and -1 if theres no collisionw
            return True  #no collision with tetromino that has already landed in the next square
        elif collision_rect.collidelist(moving_tetromino_2)!=-1 and rect.y == 0:
            running = True    
    return False  #collision with tetromino that has already landed in the next square

def moving_collide_y():
    global running
    collide1=False
    collide2=False
    for rect in moving_tetromino_1:
        collision_rect = rect.copy()  #create copy of the rect
        collision_rect.y += square_multi
        if collision_rect.collidelist(moving_tetromino_2)!=-1 and not rect.y == 0:
            #collidelist returns index of the first colliding figure and -1 if theres no collision
            collide1 = True  #no collision with tetromino that has already landed in the next square
    for rect in moving_tetromino_2:
        collision_rect = rect.copy()
        collision_rect.y += square_multi
        if collision_rect.collidelist(moving_tetromino_1)!=-1 and not rect.y == 0:
            collide2 = True
    if collide1 or collide2: 
        return True
    return False  #collision with tetromino that has already landed in the next square

def rotate_tetromino(moving_tetromino,tets = tets ,screen_x=screen_x, tetrominos_positions = tetrominos_positions, screen_y = screen_y, square = square):
    '''
    Rotates the current tetromino
    '''
    global x_offset, x_offset_1, x_offset_2
    if tets ==3: 
        return
    rotated_positions = tetrominos_positions[tets].copy() #copy the rect positions of the current tetronimo
    for i in range(len(rotated_positions)):  
            x,y = rotated_positions[i]      #read x,y-positions from the rects of the current tetronimo
            rotated_positions[i] = y,-x     #rotate x,y-positons
    if not collide_left(moving_tetromino, square) and not collide_right(moving_tetromino,screen_x, square) and not collide_landed(moving_tetromino, square) and not collide_ground(moving_tetromino, screen_y):          #only rotate when not collide with the right or left border or a landed tetromino
        tetrominos_positions[tets] = rotated_positions
    if collide_left(moving_tetromino, square) and not collide_landed(moving_tetromino, square) and not collide_ground(moving_tetromino, screen_y):
        
        tetrominos_positions[tets] = rotated_positions
        if moving_tetromino == moving_tetromino:
            if tets == 0 or tets ==5:
                x_offset += 2*square
            else:
                x_offset += square
        if moving_tetromino ==moving_tetromino_1:
            if tets == 0 or tets ==5:
                x_offset_1 += 2*square
            else:
                x_offset_1 += square
        if moving_tetromino ==moving_tetromino_2:
            if tets == 0 or tets ==5:
                x_offset_2 += 2*square
            else:
                x_offset_2 += square
            
    if collide_right(moving_tetromino, screen_x, square) and not collide_landed(moving_tetromino,square) and not collide_ground(moving_tetromino, screen_y):
        tetrominos_positions[tets] = rotated_positions
        if moving_tetromino == moving_tetromino:
            if tets == 0 or tets ==5:
                x_offset = x_offset - 2*square
            else:
                x_offset -= square
        if moving_tetromino == moving_tetromino_1:
            if tets == 0 or tets ==5:
                x_offset_1 = x_offset_1 - 2*square
            else:
                x_offset_1 -= square
        if moving_tetromino == moving_tetromino_2:
            if tets == 0 or tets ==5:
                x_offset_2 = x_offset_2 - 2*square
            else:
                x_offset_2 -= square
          
##Ränder!!

def full_rows(square=square, screen_y = screen_y, squares_width = squares_width):
    '''
    find full_rows and delete them 
    '''

    rows_to_remove = [row for row in range(screen_y - square, 0, -square) if sum(1 for tets in landed_tetrominos for rect in tets if rect.y == row) == squares_width]

    #append rects with y-value from row_to_remove list ro rects_to_remove list then remove rects from rects_to_remove list from the landed tetronimos list
    for row in rows_to_remove:
        for tets in landed_tetrominos:
            rects_to_remove = []
            [rects_to_remove.append(rect) for rect in tets if rect.y == row]
            [tets.remove(rect) for rect in rects_to_remove]
        for tets in landed_tetrominos: #move all the rects above the deleted row one square downwards
            for rect in tets:
                if rect.y <= row:
                    rect.y += square 

def text(font='Arial',font_size=10,text='',color=(255,255,255),x_position=0,y_position=0,centering=True,scale=False,scale_x=100,scale_y=100):
   '''
   text funktion to print text
   '''
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
    '''
    Mouse location safed as a Rect for collide check
    '''
    mouse_x_pos,mouse_y_pos=pygame.mouse.get_pos()
    return pygame.Rect(mouse_x_pos,mouse_y_pos,1,1)

##collide_landed_left 
##collide_landed_right

old_time = 0
old_time2 = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running = False
        if game_state=='menu':
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if mouse_location().colliderect(singleplayer_button.get_button()) and not single_player_activated:
                    singleplayer_button.text_color = (255,0,200) 
                    current_screen_size = screen_sizes['single']
                    single_player_activated = True    
                if mouse_location().colliderect(multiplayer_button.get_button()) and single_player_activated:
                    multiplayer_button.text_color = (255,0,200)
                    current_screen_size = screen_sizes['multi']
                    single_player_activated = False
                if mouse_location().colliderect(start_button.get_button()):
                    screen = pygame.display.set_mode(current_screen_size)
                    game_state = 'game'

        if game_state == 'game':
            if event.type == pygame.KEYDOWN:
                if single_player_activated:
                    if event.key == pygame.K_LEFT and not collide_left(moving_tetromino) and not collide_landed_left(moving_tetromino):
                        x_offset -= square
                    elif event.key == pygame.K_RIGHT and not collide_right(moving_tetromino, screen_x) and not collide_landed_right(moving_tetromino):
                        x_offset += square
                    elif event.key == pygame.K_DOWN and not collide_ground(moving_tetromino):
                        y_offset += square
                    elif event.key == pygame.K_UP:
                        rotate_tetromino(moving_tetromino, tets, screen_x)
                else:
                    if event.key == pygame.K_LEFT and not collide_right(moving_tetromino_2, screen_x_multi, square_multi) and not moving_collide_left() and not collide_landed_left(moving_tetromino_2):
                        x_offset_2 -= square_multi
                    elif event.key == pygame.K_RIGHT and not collide_right(moving_tetromino_2, screen_x_multi, square_multi) and not moving_collide_right() and not collide_landed_right(moving_tetromino_2):
                        x_offset_2 += square_multi
                    elif event.key == pygame.K_DOWN and not moving_collide_y():
                        y_offset_2 += square_multi
                    elif event.key == pygame.K_s and not moving_collide_y():
                        y_offset_1 += square_multi
                    elif event.key == pygame.K_UP and not moving_collide_left():
                        rotate_tetromino(moving_tetromino_2, tets2 ,screen_x_multi, tetrominos_positions_2,screen_y_multi, square_multi)
                    elif event.key == pygame.K_w and not moving_collide_left():
                        rotate_tetromino(moving_tetromino_1, tets1, screen_x_multi, tetrominos_positions, screen_y_multi, square_multi)
                    elif event.key == pygame.K_a and not collide_left(moving_tetromino_1, square_multi) and not moving_collide_right() and not collide_landed_left(moving_tetromino_1):
                        x_offset_1 -= square_multi
                    elif event.key == pygame.K_d and not collide_right(moving_tetromino_1, screen_x_multi, square_multi) and not moving_collide_left() and not collide_landed_right(moving_tetromino_1):
                        x_offset_1 += square_multi
             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state='pause'
                if event.key==pygame.K_ESCAPE:
                    running = False  

        if game_state=='pause':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_state='game'

        if game_state == 'lose':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    game_state = 'menu'
        
    #game state menu            
    if game_state=='menu':

        screen.fill("black")

        welcome_button.draw_button()

        singleplayer_button.draw_button()
        singleplayer_button.update()

        multiplayer_button.draw_button()
        multiplayer_button.update()

        if single_player_activated:
            singleplayer_button.text_color = (255,0,200)
            multiplayer_button.text_color = 'white'
        else:
            singleplayer_button.text_color = 'white'
            multiplayer_button.text_color = (255,0,200)
        
        start_button.draw_button()
        start_button.update()


        clock.tick(60)

    #game state pause
    if game_state == 'pause':

        screen.fill('black')
        pause_button.draw_button()

    
    #actual game mode
    if game_state=='game':

        if single_player_activated:

            screen.fill("black")

            #drawing the current moving tetromino
            moving_tetromino = [pygame.draw.rect(screen,tetromino_colors[tets],rects) for rects in move(y_offset,x_offset,square,screen_x,tetrominos_positions)[tets]]
##schöner           


            if not collide_ground(moving_tetromino) and not collide_landed(moving_tetromino):
                #continue to move down if there's no collision with the ground or a landed tetromino
                time = pygame.time.get_ticks()
                time_def = time - old_time
                if time_def >= 500:
                    old_time = time
                    y_offset+=square
            else:
                #if there's a collision adding tetromino to the landed tetrominos
                landed_tetrominos.extend([moving_tetromino])
                colours_landed.extend([tetromino_colors[tets]])
                tets_next=random.randint(0,6)
                if tets_next!=tets:
                    tets = tets_next
                else:
                    if tets_next!=6:
                        tets_next+=1
                    else:
                        tets_next-=1
                    tets = tets_next
                
                y_offset,x_offset=0,0 #returning to start position for the new tetromino    
                x_offset=0
                moving_tetromino=[] #only one moving tetromino 

            #drawing the landed tetrominos
            [pygame.draw.rect(screen,colours_landed[i],landed_tetrominos[i][j]) for i in range(len(landed_tetrominos)) for j in range(len(landed_tetrominos[i]))]

            full_rows()
        
            draw_grid(grid_squares)
            clock.tick(120)

        if not single_player_activated:

            screen.fill("black")

            moving_tetromino_1 = [pygame.draw.rect(screen,tetromino_colors[tets1],rects) for rects in move(y_offset_1,x_offset_1,square_multi,screen_x_multi,tetrominos_positions,start='left')[tets1]]

            moving_tetromino_2 = [pygame.draw.rect(screen,tetromino_colors[tets2],rects) for rects in move(y_offset_2,x_offset_2,square_multi,screen_x_multi,tetrominos_positions_2,start='right')[tets2]]

            if not collide_ground(moving_tetromino_1, screen_y_multi) and not collide_landed(moving_tetromino_1, square_multi):
                time = pygame.time.get_ticks()
                time_def = time - old_time
                if time_def >= 500:
                    old_time = time
                    y_offset_1 += square_multi
            else:
                #if there's a collision adding tetromino to the landed tetrominos
                landed_tetrominos.extend([moving_tetromino_1])
                colours_landed.extend([tetromino_colors[tets1]])
                tets_next_1=random.randint(0,6)
                if tets_next_1!=tets1:
                    tets1 = tets_next_1
                else:
                    if tets_next_1!=6:
                        tets_next_1+=1
                    else:
                        tets_next_1-=1
                    tets1 = tets_next_1
                
                y_offset_1,x_offset_1=0,0 #returning to start position for the new tetromino    
                x_offset_1=0
                moving_tetromino_1=[] #only one moving tetromino 

              


            if not collide_ground(moving_tetromino_2, screen_y_multi) and not collide_landed(moving_tetromino_2, square_multi):
                time2 = pygame.time.get_ticks()
                time_def2 = time2 - old_time2
                if time_def2 >= 500:
                    old_time2 = time2
                    y_offset_2 += square_multi

            else:
                #if there's a collision adding tetromino to the landed tetrominos
                landed_tetrominos.extend([moving_tetromino_2])
                colours_landed.extend([tetromino_colors[tets2]])
                tets_next_2=random.randint(0,6)
                if tets_next_2!=tets2:
                    tets2 = tets_next_2
                else:
                    if tets_next_2!=6:
                        tets_next_2+=1
                    else:
                        tets_next_2-=1
                    tets2 = tets_next_2
                
                y_offset_2,x_offset_2=0,0 #returning to start position for the new tetromino    
                x_offset_2=0
                moving_tetromino_2=[] #only one moving tetromino


            [pygame.draw.rect(screen,colours_landed[i],landed_tetrominos[i][j]) for i in range(len(landed_tetrominos)) for j in range(len(landed_tetrominos[i]))]

            full_rows(square_multi, screen_y_multi, squares_width_multi)

            draw_grid(grid_squares_multi)
            clock.tick(120)

    if game_state == 'lose':

        screen.fill('black')
        lose_button.draw_button()

        clock.tick(60)

    pygame.display.flip()

pygame.quit()


