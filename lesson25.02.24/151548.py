import pygame
import random


W,H  = 500, 500

pygame.init()
win = pygame.display.set_mode((W,H))

object_to_draw = ""

win.fill((255,255,255))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    


    #pygame.draw.circle(win, random.choices(range(256), k = 3), (W / 2, H / 2), 30)
    #pygame.draw.rect(win, random.choices(range(256), k=3), (0,0,50,50))
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        object_to_draw = 'квадрат'
    if keys[pygame.K_w]:
        object_to_draw = 'круг'
    if keys[pygame.K_SPACE]:
        object_to_draw = 'пусто'

    mesto = pygame.mouse.get_pos()
    if object_to_draw == 'квадрат':
        pygame.draw.rect(win, random.choices(range(256), k=3), (mesto[0], mesto[1], 50, 50))
    if object_to_draw == 'круг':
        pygame.draw.circle(win, random.choices(range(256), k=3), (mesto[0], mesto[1]), 30)
    if object_to_draw == 'пусто':
        win.fill((255,255,255))


    pygame.display.update()


    pygame.time.delay(20)
