from Game import constants


def collisions_detection(first_player_racket, second_player_racket, ball) -> None:
    if ball.y > constants.SCREEN_HEIGHT / 2:
        if ball.colliderect(first_player_racket):
            ball.y_speed *= -1
    if ball.y < constants.SCREEN_HEIGHT / 2:
        if ball.colliderect(second_player_racket):
            ball.y_speed *= -1
