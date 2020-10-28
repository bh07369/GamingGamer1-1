import pygame as pg
import random

WIDTH = 360
HEIGHT = 480
FPS = 60

#Hurr durr colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Gaming Gamers")

clock = pg.time.Clock()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        screen.fill(BLACK)
        pg.display.flip()
pg.quit()

