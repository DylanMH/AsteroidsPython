import pygame as pg
import random
from bullet import Bullet

class Player():
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.load_image = pg.image.load("images/main_ship.png").convert_alpha()
        self.scaled_image = pg.transform.scale(self.load_image, (100, 80))
        self.image = self.scaled_image
        start_buffer = 300
        self.rect = self.image.get_rect(
            center = (screen_rect.centerx, screen_rect.centery + start_buffer)
        )
        self.dx = 300
        self.dy = 300
        self.bullets = []
        self.timer = 0.0
        self.bullet_delay = 500
        self.add_bullet = False
    
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if self.add_bullet:
                    self.bullets.append(Bullet(self.rect.center, self.screen_rect))
                    self.add_bullet = False

    def update(self, keys, dt):
        self.rect.clamp_ip(self.screen_rect)
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.x -= self.dx * dt
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.x += self.dx * dt
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rect.y -= self.dy * dt
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rect.y += self.dy * dt
        if pg.time.get_ticks() - self.timer > self.bullet_delay:
            self.timer = pg.time.get_ticks()
            self.add_bullet = True

    def draw(self, surf):
        for bullet in self.bullets:
                bullet.render(surf)
        surf.blit(self.image, self.rect)
