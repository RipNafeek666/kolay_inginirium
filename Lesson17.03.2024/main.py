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
img = load_img('inzh.png')
img1 = pg.transform.scale(img, (200,200))
img2 = pg.transform.scale(img, (700,700))

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    win.fill('#dbf6e9')
    win.blit(img1, (0,0))
    win.blit(img2, (100, 100))
    pg.display.update()
