import random

import pygame

pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
BALL_SPEED_X = 2
BALL_SPEED_Y = 2

player_score = 0
enemy_score = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Ping-Pong")

player = pygame.Rect(SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT - 25, 50, 5)
ball = pygame.Rect(SCREEN_WIDTH / 2 - 5, SCREEN_HEIGHT / 2 - 5, 10, 10)
enemy = pygame.Rect(SCREEN_WIDTH / 2 - 25, 25, 50, 5)
bg_color = pygame.Color('grey12')


def ball_animation():
    global BALL_SPEED_X, BALL_SPEED_Y, player_score, enemy_score

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        if ball.y <= 0.5:
            player_score += 1
            pygame.mixer.music.load("Materials/ping_pong_8bit_peeeeeep.ogg")
            pygame.mixer.music.play()
            ball_restart()
        if ball.y >= 710:
            enemy_score += 1
            pygame.mixer.music.load("Materials/ping_pong_8bit_peeeeeep.ogg")
            pygame.mixer.music.play()
            ball_restart()

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        pygame.mixer.music.load("Materials/ping_pong_8bit_plop.ogg")
        pygame.mixer.music.play()
        BALL_SPEED_X *= -1

    if ball.colliderect(player) or ball.colliderect(enemy):
        pygame.mixer.music.load("Materials/ping_pong_8bit_beeep.ogg")
        pygame.mixer.music.play()
        BALL_SPEED_Y *= -1


def ball_restart():
    global BALL_SPEED_Y, BALL_SPEED_X
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    BALL_SPEED_Y *= random.choice((1, -1))
    BALL_SPEED_X *= random.choice((1, -1))


def player_animation():
    if player.left <= 0:
        player.left = 0
    if player.right >= SCREEN_WIDTH:
        player.right = SCREEN_WIDTH


def enemy_animation():
    if enemy.left <= 0:
        enemy.left = 0
    if enemy.right >= SCREEN_WIDTH:
        enemy.right = SCREEN_WIDTH


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 300 * dt
    if keys[pygame.K_d]:
        player.x += 300 * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        enemy.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        enemy.x += 300 * dt

    ball_animation()
    player_animation()
    enemy_animation()

    screen.fill(bg_color)
    pygame.draw.rect(screen, 'gray', player)
    pygame.draw.ellipse(screen, 'gray', ball)
    pygame.draw.rect(screen, 'gray', enemy)
    pygame.draw.aaline(screen, 'gray', (SCREEN_HEIGHT, SCREEN_HEIGHT / 2), (0, SCREEN_HEIGHT / 2))
    screen.blit(
        pygame.font.SysFont('arial', 30, bold=True).render(f'score: {player_score} - {enemy_score}', True, 'white'),
        (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2))

    pygame.display.flip()

    dt = clock.tick(120) / 700

pygame.quit()
