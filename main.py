import pygame as pg
from parameters import screen, W, H
import player
import globals

pg.init()

clock = pg.time.Clock()

player = player.Player(50, 50, 0.8)

colours = {'bg': "#F2EDD7", 'ground': "#755139"}

run = True

while run:

    clock.tick(60)

    screen.fill(colours['bg'])

    pg.draw.rect(screen, colours['ground'], pg.Rect(0, globals.GROUND_LEVEL, W, H - globals.GROUND_LEVEL))

    player.update()
    player.draw()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                globals.moving_right = True
                stay = False
            if event.key == pg.K_LEFT:
                globals.moving_left = True
                stay = False
            if event.key == pg.K_UP:
                globals.jumping = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                globals.moving_right = False
                stay = True
            if event.key == pg.K_LEFT:
                globals.moving_left = False
                stay = True

    pg.display.flip()
