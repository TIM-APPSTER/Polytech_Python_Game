# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen_width = 720
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Ping-Pong")

player = pygame.Rect(screen_width / 2 - 15, screen_height / 2 + 300, 50, 5)
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 10, 10)
enemy = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 300, 50, 5)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.draw.rect(screen, 'gray', player)

    pygame.draw.ellipse(screen, 'gray', ball)
    pygame.draw.rect(screen, 'gray', enemy)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 300 * dt
    if keys[pygame.K_d]:
        player.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(120) / 700

pygame.quit()
