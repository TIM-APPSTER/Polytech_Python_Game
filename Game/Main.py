# Example file showing a basic pygame "game loop"
import pygame


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, enemy_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(enemy):
        ball_speed_y *= -1

    if ball.y <= 0.5:
        player_score += 1
    if ball.y >= 710:
        enemy_score += 1


def player_animation():
    if player.left <= 0:
        player.left = 0
    if player.right >= screen_width:
        player.right = screen_width


def enemy_animation():
    if enemy.left <= 0:
        enemy.left = 0
    if enemy.right >= screen_width:
        enemy.right = screen_width


# pygame setup
pygame.init()
screen_width = 720
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Ping-Pong")

player = pygame.Rect(screen_width / 2 - 25, screen_height - 25, 50, 5)
ball = pygame.Rect(screen_width / 2 - 5, screen_height / 2 - 5, 10, 10)
enemy = pygame.Rect(screen_width / 2 - 25, 25, 50, 5)
bg_color = pygame.Color('grey12')

ball_speed_x = 2
ball_speed_y = 2
player_score = 0
enemy_score = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(bg_color)
    pygame.draw.rect(screen, 'gray', player)
    pygame.draw.ellipse(screen, 'gray', ball)
    pygame.draw.rect(screen, 'gray', enemy)
    pygame.draw.aaline(screen, 'gray', (screen_height, screen_height / 2), (0, screen_height / 2))
    screen.blit(
        pygame.font.SysFont('arial', 30, bold=True).render(f'score: {player_score} - {enemy_score}', True, 'white'),
        (screen_width / 2 - 50, screen_height / 2))

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(120) / 700

pygame.quit()
