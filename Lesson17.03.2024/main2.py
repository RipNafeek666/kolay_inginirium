import random

import pygame as pg

pg.init()
size = W, H = 700, 700
FPS = 30
win = pg.display.set_mode(size)

img = pg.image.load('inzh.png   ')

def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0,0))
    img.set_colorkey(colorkey)
    return img
img = load_img('inzh.png')
img = pg.transform.scale(img, (100,100))
all_sprites = pg.sprite.Group()

for i in range(100):
    sprite = pg.sprite.Sprite(all_sprites)
    sprite.image = img
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = random.randrange(W)
    sprite.rect.y = random.randrange(H)
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    win.fill((255,255,255))
    all_sprites.draw(win)
    pg.display.update()
