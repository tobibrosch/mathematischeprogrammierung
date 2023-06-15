import pygame

class CustomObject:
    def __init__(self, rects, color):
        self.rects = rects
        self.color = color

    def draw(self, screen):
        for rect in self.rects:
            pygame.draw.rect(screen, self.color, rect)

    def move(self, dx, dy):
        for rect in self.rects:
            rect.x += dx
            rect.y += dy

    def rotate(self, angle):
        # Implementiere hier die Logik zur Rotation der Rechtecke
        pass

# Beispielverwendung
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Erstelle einige Rechtecke
rect_1 = pygame.Rect(100, 100, 50, 50)
rect_2 = pygame.Rect(200, 200, 100, 50)
rect_3 = pygame.Rect(300, 300, 80, 80)

# Füge die Rechtecke zu einem Objekt zusammen
custom_object = CustomObject([rect_1, rect_2, rect_3], (255, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))  # Hintergrund löschen

    # Zeichne das benutzerdefinierte Objekt auf dem Bildschirm
    custom_object.draw(screen)

    pygame.display.flip()
    clock.tick(60)
