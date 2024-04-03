import pygame

import constants
from game_objects import Racket, Ball, DrawScore, draw_dotted_line
from game_logic import collisions_detection

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
screen.fill(constants.SCREEN_COLOR)

first_player_racket = Racket(screen, constants.FIRST_PLAYER_COORDINATE[0], constants.FIRST_PLAYER_COORDINATE[1],
                             pygame.K_a,
                             pygame.K_d)
first_player_score = DrawScore(screen, None, 36)

second_player_racket = Racket(screen, constants.SECOND_PLAYER_COORDINATE[0], constants.SECOND_PLAYER_COORDINATE[1],
                              pygame.K_LEFT,
                              pygame.K_RIGHT)
second_player_score = DrawScore(screen, None, 36)

ball = Ball(screen, 4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(constants.SCREEN_COLOR)
    draw_dotted_line(screen, 'white')
    first_player_score.draw(first_player_racket.player_score, constants.SCREEN_WIDTH / 2,
                            constants.SCREEN_HEIGHT / 2 - 30)

    first_player_racket.draw()
    first_player_racket.moving()

    second_player_score.draw(second_player_racket.player_score, constants.SCREEN_WIDTH / 2,
                             constants.SCREEN_HEIGHT / 2 + 30)
    second_player_racket.draw()
    second_player_racket.moving()

    ball.draw()
    ball.moving()

    collisions_detection(first_player_racket, second_player_racket, ball)

    pygame.display.update()
    clock.tick(constants.FPS)
