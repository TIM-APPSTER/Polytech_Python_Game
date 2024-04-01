import pygame

import constants
from game_objects import PlayerRackets
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
screen.fill(constants.SCREEN_COLOR)


player_rackets = PlayerRackets(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(constants.SCREEN_COLOR)


    player_rackets.draw()
    player_rackets.move(5)
    pygame.display.flip()
    clock.tick(constants.FPS)
