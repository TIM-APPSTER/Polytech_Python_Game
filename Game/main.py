import pygame

import constants
from game_objects import Racket, Ball
from game_logic import collisions_detection

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
screen.fill(constants.SCREEN_COLOR)

first_player_coordinate = (constants.SCREEN_WIDTH / 2 - 25, constants.SCREEN_HEIGHT - 25)
first_player_racket = Racket(screen, first_player_coordinate[0], first_player_coordinate[1], pygame.K_a,
                             pygame.K_d)

second_player_coordinate = (constants.SCREEN_WIDTH / 2 - 25, 25)
second_player_racket = Racket(screen, second_player_coordinate[0], second_player_coordinate[1], pygame.K_LEFT,
                              pygame.K_RIGHT)

ball = Ball(screen, 4)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(constants.SCREEN_COLOR)

    first_player_racket.draw()
    first_player_racket.moving()

    second_player_racket.draw()
    second_player_racket.moving()

    ball.draw()
    ball.moving()

    collisions_detection(first_player_racket, second_player_racket, ball)

    pygame.display.update()
    clock.tick(constants.FPS)
