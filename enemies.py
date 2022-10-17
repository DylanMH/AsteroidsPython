import math
import pygame as pg
import random

class Enemy:
    def __init__(self, screen_rect):
        self.random_size = (random.randint(25,150), random.randint(25, 150))
        self.screen_rect = screen_rect
        self.image = pg.image.load("images/asteroid_brown.png").convert_alpha()
        self.transformed_image = pg.transform.scale(self.image, self.random_size)
        start_buffer = -100
        self.rect = self.image.get_rect(
            center = (screen_rect.centerx, screen_rect.centery + start_buffer)
        )
        self.distance_above_player = 0
        self.speed = 2

    def pos_towards_player(self, player_rect):
        c = math.sqrt((player_rect.x - self.rect.x) ** 2 + (player_rect.y - self.distance_above_player - self.rect.y) ** 2)
        try:
            x = (player_rect.x - self.rect.x) / c
            y = ((player_rect.y - self.distance_above_player) - self.rect.y) / c
        except ZeroDivisionError:
            return False
        return (x, y)
 
    def update(self, dt, player):
        new_pos = self.pos_towards_player(player.rect)
        if new_pos:
            self.rect.x, self.rect.y = (self.rect.x + new_pos[0] * self.speed, self.rect.y + new_pos[1] * self.speed)
        pass

    def draw(self, surf):
        surf.blit(self.transformed_image, self.rect)