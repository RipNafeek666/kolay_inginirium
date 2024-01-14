import pygame

pygame.init()
win = pygame.display.set_mode((600, 400))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (255, 255, 255)
    win.fill(color)
    pygame.draw.rect(win, (25, 91, 54), (x,y,w,h))
    pygame.draw.line(win, (0 , 255, 255), (0, 0), (100, 100),5)
    pygame.draw.circle(win, (255, 0 , 0), (200, 200), 50)
    pygame.draw.lines(win, (0, 0, 0), True, ((200, 200), (300, 150), (300, 250)), 10)
    pygame.display.update()
