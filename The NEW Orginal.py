import pygame as pg
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 60

#UNVISITY
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9
vec = pg.math.Vector2
GROUND = HEIGHT-30

#DEFINE COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#ASSET FOLDERS
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#Platform Class
class Platform(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((150, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT-75)

    def update(self):
        self.rect.x += -5
        if self.rect.right < 0:
            self.rect.left = WIDTH
            
#PLAYER CLASS
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "p1-jump.png ")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        self.pos = vec(10, GROUND - 60)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        

    def update(self):

        self.acc = vec(0, PLAYER_GRAV)

        #RETURNS A LIST, KEYSTATE, OF ALL PRESSED KEYS
        keystate = pg.key.get_pressed()

        #CHECKS TO SEE WHICH KEYS WERE IN THE LIST
        if keystate[pg.K_RIGHT]:
            self.acc.x += PLAYER_ACC
        if keystate[pg.K_LEFT]:
            self.acc.x -= PLAYER_ACC
        if keystate[pg.K_UP]:
            self.rect.y += 5
        if keystate[pg.K_DOWN]:
            self.rect.y += 5
        if self.vel.y == 0 and keystate[pg.K_SPACE]:
            self.vel.y = -20

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.y > GROUND:
            self.pos.y = GROUND + 1
            self.vel.y = 0

        self.rect.midbottom = self.pos

#INITIALIZE VARIABLES  
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("MY GAME")

clock = pg.time.Clock()

#ADD BACKROUND
bkgr_image = pg.image.load(os.path.join(img_folder, "backround.jpg")).convert()
backround = pg.transform.scale(bkgr_image, (WIDTH, HEIGHT))
backgroung_rect = backround.get_rect()

#SPRITE GROUPS
all_sprites = pg.sprite.Group()
player = Player()
platform = Platform()
all_sprites.add(platform)
all_sprites.add(player)

#GAME LOOP:
#  PROCESS EVENTS
#  UPDATE
#  DRAW
running = True
while running:

    clock.tick(FPS)

    #PROCESS EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #UPDATES
    all_sprites.update()

    #DRAW
    screen.blit(backround, backgroung_rect)
    all_sprites.draw(screen)

    #FLIP AFTER DRAWING
    pg.display.flip()
    
#CONSTANTS - PHYSICS
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9
vec = pg.math.Vector2



pg.quit()      
    
