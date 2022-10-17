import pygame as pg

import enemies
import main_player
import bullet

pg.init()

screen = pg.display.set_mode((800, 600))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
enemy = enemies.Enemy(screen_rect)
player = main_player.Player(screen_rect)

running = True
while running:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        player.get_event(event)
    screen.fill((0, 0, 0))
    delta_time = clock.tick(60)/1000.0
    player.update(keys, delta_time)
    enemy.update(delta_time, player)
    player.draw(screen)
    enemy.draw(screen)
   
    pg.display.update()

