import pygame as pg

class Bullet:
    def __init__(self, loc, screen_rect):
        self.screen_rect = screen_rect
        self.image = pg.Surface((5, 40)).convert_alpha()
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = loc)

    #def update(self):
        #self.speed = 5
        #self.rect.y += self.speed
        #print("Testing Bullet Velocity")

    def render(self, surf):
        self.speed = 5
        self.rect.y -= self.speed
        surf.blit(self.image, self.rect)