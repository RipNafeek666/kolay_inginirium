import random
import sqlite3 as sql
import pygame as pg

con = sql.connect("score.sqlaite")
cur = con.cursor()

def create_database(name):
    que_create = '''
        CREATE TABLE IF NOT EXISTS score(
            id INTEGER PRIMARY KEY,
            name TEXT ,
            score INTEGER
        )    
    '''

    cur.execute(que_create)
    con.commit()

create_database()
pg.init()

def insert_data(name,score):
    que_insert = '''
        INSERT INTO score (name, score) VALUES
        ('{}', {})
    '''

    cur.execute(que_insert.format(name, score))
    con.commit()


width = 500
height = 500
win = pg.display.set_mode((width, height))

class Player(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pg.image.load('player.png')
        self.image = pg.transform.scale(self.image, (120,90))
        self.rect = self.image.get_rect()

    def update(self):
        self.move_by_keys()

    def move_by_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.top -= 5
        if keys[pg.K_DOWN]:
            self.rect.top += 5
        if keys[pg.K_LEFT]:
            self.rect.left -= 5
        if keys[pg.K_RIGHT]:
            self.rect.left += 5

class Enemy(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pg.image.load('b.webp')
        self.image = pg.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.right = width


all_sprites = pg.sprite.Group()
player = Player(all_sprites)

enemy_sprites = pg.sprite.Group()
enemy =Enemy(enemy_sprites)

FPS = 60
clock = pg.time.Clock()
score = 0

name = input('введите ваше имя:')


font = pg.font.Font(None, 36)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            insert_data(name,score)
            exit()
    text = font.render(str(score), True,(180,0,0))
    win.fill((255,255,255))
    hits = pg.sprite.spritecollide(player,enemy_sprites,False)
    if len(hits) > 0:
        score += 1
        hits[0].rect.left = random.randint(0, width - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, height - hits[0].rect.height)

    all_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.draw(win)
    enemy_sprites.update()
    win.blit(text,(0,0))
    pg.display.update()
    clock.tick(FPS)