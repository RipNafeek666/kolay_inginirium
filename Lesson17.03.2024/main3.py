import random

import pygame as pg

pg.init()
size = W, H = 700, 700
FPS = 30
win = pg.display.set_mode(size)

img = pg.image.load('inzh.png')

def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0,0))
    img.set_colorkey(colorkey)
    return img

class Inginirium(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_img("inzh.png")
        self.image = pg.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

all_sprites = pg.sprite.Group()
for i in range(50):
    Inginirium(all_sprites)
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()


    win.fill((255,255,255))
    all_sprites.draw(win)
    all_sprites.update()
    pg.display.update()
