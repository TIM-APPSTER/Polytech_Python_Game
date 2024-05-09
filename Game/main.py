import pygame

import constants
from game_logic import collisions_detection
from game_objects import Racket, Ball, draw_dotted_line, draw_countdown
from menu import Menu

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

ball = Ball(screen)
is_pause = False

menu = Menu(screen)

count_flag = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu.is_show = True
    if menu.is_show:
        menu.show_menu()
    else:
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
            count_flag = True
            score_time = pygame.time.get_ticks()
            first_player_racket.score += 1
        elif ball.bottom >= constants.SCREEN_HEIGHT + 15:
            count_flag = True
            score_time = pygame.time.get_ticks()
            second_player_racket.score += 1

        first_player_racket.draw_score(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 50)
        second_player_racket.draw_score(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 50)

        if count_flag:
            current_time = pygame.time.get_ticks()
            ball.x = constants.SCREEN_WIDTH / 2
            ball.y = constants.SCREEN_HEIGHT / 2
            draw_countdown(screen, score_time)  # Pass score_time to the function
            if current_time - score_time >= 2100:
                count_flag = False  # Reset count_flag when countdown is done
        pygame.display.update()

    clock.tick(constants.FPS)
