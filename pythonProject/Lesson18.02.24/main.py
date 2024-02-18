import random

import pygame

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))



class Circle:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.dir = 'right'

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def horizontal_movements(self):
        if self.dir == 'right':
            self.x += 1
            if self.x > width:
                self.dir = 'left'
        else:
            self.x -= 1
            if self.x < 0:
                self.dir = 'right'

krugi = []
for i in range(100):
    krugi.append(Circle(random.choices(range(256), k = 3), i * 10, i * 5, 30))

FPS = 60
cloclk = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255,255,255))

    for i in range(len(krugi)):
        krugi[i].draw()
        krugi[i].horizontal_movements()

    pygame.display.update()
    cloclk.tick(FPS)
