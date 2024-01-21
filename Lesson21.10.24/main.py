import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 100
y = 50
x1 = 100
y1 = 50

direction = 1
direction1 = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = x + direction
    y1 = y1 + direction1
    if y1 > 500:
        direction1 = -1
    if y1 < 0:
        direction1 = 1
    if x > 500:
        direction = -1
    if x < 0:
        direction = 1
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x, y, 100, 150))
    pygame.draw.circle(win, (255, 0, 0), (x1, y1), 30)
    pygame.display.update()

    pygame.time.delay(10)
