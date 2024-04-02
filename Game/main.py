import pygame

import constants
from game_objects import Racket, Ball

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
screen.fill(constants.SCREEN_COLOR)

first_player_coordinate = (constants.SCREEN_WIDTH / 2 - 25, constants.SCREEN_HEIGHT - 25)
first_player_racket = Racket(screen, first_player_coordinate[0], first_player_coordinate[1], pygame.K_a,
                             pygame.K_d)

second_player_coordinate = (constants.SCREEN_WIDTH / 2 - 25, 25)
second_player_rackets = Racket(screen, second_player_coordinate[0], second_player_coordinate[1], pygame.K_LEFT,
                               pygame.K_RIGHT)

ball = Ball(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(constants.SCREEN_COLOR)

    first_player_racket.draw()
    first_player_racket.move()

    second_player_rackets.draw()
    second_player_rackets.move()

    ball.draw()
    ball.move()

    pygame.display.flip()
    clock.tick(constants.FPS)
