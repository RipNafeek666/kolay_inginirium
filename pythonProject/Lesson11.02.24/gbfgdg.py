import pygame

class Circle:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), 30)
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 3
        if keys[pygame.K_RIGHT]:
            self.x += 3
        if keys[pygame.K_UP]:
            self.y -= 3
        if keys[pygame.K_DOWN]:
            self.y += 3

pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))

x = 0
y = 0

circle = Circle((255, 55, 0), 0, 0, 30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    win.fill((255, 255, 255))
    circle.move_by_keys()
    circle.draw()
    pygame.display.update()
    pygame.time.delay(10)
