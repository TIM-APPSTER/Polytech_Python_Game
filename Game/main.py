import pygame

import constants
from game_logic import collisions_detection
from game_objects import Racket, Ball, draw_dotted_line

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
screen.fill(constants.SCREEN_COLOR)

first_player_racket = Racket(screen, constants.FIRST_PLAYER_COORDINATE[0], constants.FIRST_PLAYER_COORDINATE[1],
                             pygame.K_a,
                             pygame.K_d)

second_player_racket = Racket(screen, constants.SECOND_PLAYER_COORDINATE[0], constants.SECOND_PLAYER_COORDINATE[1],
                              pygame.K_LEFT,
                              pygame.K_RIGHT)

ball = Ball(screen, 4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(constants.SCREEN_COLOR)
    draw_dotted_line(screen, 'white')

    first_player_racket.draw()
    first_player_racket.moving()

    second_player_racket.draw()
    second_player_racket.moving()

    ball.draw()
    ball.moving()

    collisions_detection(first_player_racket, second_player_racket, ball)

    if ball.top <= -12:
        first_player_racket.score += 1
    elif ball.bottom >= constants.SCREEN_HEIGHT + 15:
        second_player_racket.score += 1

    first_player_racket.draw_score(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 50)
    second_player_racket.draw_score(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 50)
    pygame.display.update()
    clock.tick(constants.FPS)
