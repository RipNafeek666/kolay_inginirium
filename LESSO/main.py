import random

import pygame as pg

pg.init()

class Enemy(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pg.image.load('b.webp')
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.left -= 5
        if keys[pg.K_RIGHT]:
            self.rect.left += 5
        if keys[pg.K_UP]:
            self.rect.top -= 5
        if keys[pg.K_DOWN]:
            self.rect.top += 5

class Player(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pg.image.load('ing.png')
        self.image = pg.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect()
    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.left -= 5
        if keys[pg.K_d]:
            self.rect.left += 5
        if keys[pg.K_w]:
            self.rect.top -= 5
        if keys[pg.K_s]:
            self.rect.top += 5
width = 500
height = 500

win = pg.display.set_mode((width, height))

background = pg.image.load("1e47fef9674414a9fbdb5f4ddb4247ee.png")
background = pg.transform.scale(background, (width, height))

all_sprites = pg.sprite.Group()
player = Player(all_sprites)
enemy_sprites = pg.sprite.Group()
enemy = Enemy(enemy_sprites)

font = pg.font.Font(None, 36)
text = font.render('Привет', True, (255,255,255))

sound = pg.mixer.Sound('pew_pew-dknight556-1379997159.mp3')
sound.play()
FPS = 60
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    win.fill((255,255,255))
    win.blit(background,(0,0))
    win.blit(text, (0,0))
    all_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.draw(win)
    enemy_sprites.update()

    hits = pg.sprite.spritecollide(player, enemy_sprites, False)
    if len(hits) > 0:
        hits[0].rect.left = random.randint(0, width - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, height - hits[0].rect.height)

    pg.display.update()
    clock.tick(FPS)