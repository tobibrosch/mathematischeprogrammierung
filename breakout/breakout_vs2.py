import pygame
import random
from math import sqrt
def moving_rect(dt):
    global x_speed, y_speed, y_speed_rect2,rectangle_list,dx,dy
    rect_1.x += x_speed * dt * dx
    rect_1.y += y_speed * dt * dy
    rect_2.y += y_speed_rect2 * dt
    pygame.draw.rect(screen, "red", rect_1)
    pygame.draw.rect(screen, "white", rect_2)
    if rect_1.top < 0:
        y_speed *= -1
    if rect_1.bottom > 800:
        rect_1.x, rect_1.y = 400, 400
    if rect_1.left < 0 or rect_1.right > 800:
        x_speed *= -1
    hitbox = 10
    for rect in rectangle_list:
        if rect_1.colliderect(rect):
            if rect!=rect_2:
                rectangle_list.remove(rect)  # Entferne das Rechteck aus der Liste
            if rect==rect_2:
                dy = random.randint(5,10)/10
                dx = round(sqrt(1-dy**2),4)
            if abs(rect_1.bottom - rect.top) < hitbox and y_speed > 0:
                y_speed *= -1
            if abs(rect_1.top - rect.bottom) < hitbox and y_speed < 0:
                y_speed *= -1
            if abs(rect_1.left - rect.right) < hitbox and x_speed < 0:
                x_speed *= -1
            if abs(rect_1.right - rect.left) < hitbox and x_speed > 0:
                x_speed *= -1
pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
rect_1 = pygame.Rect(400, 400, 10, 10)
rect_2 = pygame.Rect(200, 700, 100, 10)


#rectangle_list = [rect_3, rect_4]
rectangle_list = [pygame.Rect(i*100+5,j*25,90,20) for i in range(8) for j in range(8)]
rectangle_list.append(rect_2)
#Geschwindigkeiten
x_speed = 400
y_speed = 400
y_speed_rect2 = 0
x_speed_rect2 = 0
dx =1
dy =1
while running:
    # Beende durch X drücken oder q
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_keys[pygame.K_q]:
            running = False
    screen.fill("black")

    dt = clock.tick(120) / 1000

    if pressed_keys[pygame.K_a] and rect_2.left > 0:
        rect_2.x -= 600 * dt
    if pressed_keys[pygame.K_d] and rect_2.right < 800:
        rect_2.x += 600 * dt

    for brick in rectangle_list:
        pygame.draw.rect(screen, "purple" ,brick)


    moving_rect(dt)


    pygame.display.flip()
    clock.tick(120)

pygame.quit()
