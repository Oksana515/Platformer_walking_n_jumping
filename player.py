import pygame as pg
from parameters import screen, W
import globals


class Player:
    def __init__(self, x0, y0, scale):
        self.images = []
        self.frame_index = 0
        self.animation_cooldown = 120
        self.update_time = pg.time.get_ticks()
        for i in range(5):
            img = pg.image.load(f'img/{i}.png')
            w = int(img.get_width()) * scale
            h = int(img.get_height()) * scale
            img = pg.transform.scale(img, (w, h))
            self.images.append(img)
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x0
        self.rect.y = y0
        self.flip = False
        # variables for vertical movement
        self.vel_y = 0
        self.max_vel = - 15
        self.gravity = 0.5
        self.on_the_ground = False
        self.in_the_air = True

    def update(self):
        if globals.moving_right and self.rect.right <= W:
            self.rect.x += 4
            self.flip = False
            self.animate()
        else:
            self.image = self.images[0]
        if globals.moving_left and self.rect.left >= 0:
            self.rect.x -= 4
            self.flip = True
            self.animate()
        else:
            pg.transform.flip(self.images[0], True, False)
        if self.in_the_air:
            self.vel_y += self.gravity
            self.rect.y += self.vel_y
            self.image = self.images[4]
        # check collision with the ground
        if self.rect.bottom > globals.GROUND_LEVEL:
            self.rect.bottom = globals.GROUND_LEVEL
            self.on_the_ground = True
            self.in_the_air = False
            globals.jumping = False
            self.vel_y = 0
        if globals.jumping and self.on_the_ground:
            self.vel_y = self.max_vel
            self.on_the_ground = False
            self.in_the_air = True

    def animate(self):
        self.image = self.images[self.frame_index]
        # check if enough time has passed since the last update
        if pg.time.get_ticks() - self.update_time > self.animation_cooldown:
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= 4:
                self.frame_index = 0

    def draw(self):
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)

