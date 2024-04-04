import pygame

import constants


class Racket(pygame.Rect):
    def __init__(self, screen: pygame.display.set_mode, x: int, y: int, left_key, right_key):
        super().__init__(x, y, 50, 5)
        self.x_spawn = x
        self.y_spawn = y
        self.left_key = left_key
        self.right_key = right_key
        self.speed = 1
        self.dt = 5
        self.score = 0
        self.screen = screen

    def moving(self):
        keys = pygame.key.get_pressed()
        if keys[self.left_key]:
            self.x -= self.speed * self.dt
        if keys[self.right_key]:
            self.x += self.speed * self.dt

        if self.left <= 0:
            self.left = 0
        if self.right >= constants.SCREEN_WIDTH:
            self.right = constants.SCREEN_WIDTH

    def draw(self):
        pygame.draw.rect(self.screen, 'gray', self)

    def draw_score(self, x, y):
        font = pygame.font.Font(None, 50)
        text = font.render(f"{self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)


class Ball(pygame.Rect):
    def __init__(self, screen, speed):
        self.x_spawn = constants.SCREEN_WIDTH / 2
        self.y_spawn = constants.SCREEN_HEIGHT / 2
        super().__init__(self.x_spawn, self.y_spawn, 10, 10)
        self.radius = 5
        self.x_speed = speed
        self.y_speed = speed
        self.dt = 5
        self.screen = screen

    def moving(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.top <= -15 or self.bottom >= constants.SCREEN_HEIGHT + 20:
            self.restart()
        if self.left <= 0 or self.right >= constants.SCREEN_WIDTH:
            self.x_speed *= -1

    def restart(self):
        self.x = self.x_spawn
        self.y = self.y_spawn
        self.countdown()

    def countdown(self):
        countdown_numbers = [3, 2, 1]
        font = pygame.font.Font(None, 200)  # Use default font, size 500
        x = constants.SCREEN_WIDTH / 2
        y = constants.SCREEN_HEIGHT / 2

        for number in countdown_numbers:
            # Create a semi-transparent surface for the text
            countdown_text = font.render(str(number), True, (255, 255, 255))  # White text
            text_surface = pygame.Surface(countdown_text.get_size(), pygame.SRCALPHA)
            text_surface.blit(countdown_text, (0, 0))
            text_surface.set_alpha(128)  # Set alpha to 128 (half-transparent)

            # Get text rectangle for positioning
            countdown_rect = text_surface.get_rect()
            countdown_rect.center = (x, y)

            self.screen.fill('black')

            pygame.display.update(self.screen.blit(text_surface, countdown_rect))

            pygame.time.wait(1000)

    def draw(self):
        pygame.draw.ellipse(self.screen, 'gray', self)


def draw_dotted_line(screen, line_color):
    start_x, start_y = (0, constants.SCREEN_HEIGHT / 2)
    segment_length = 5
    spacing = 10
    for x in range(start_x, constants.SCREEN_WIDTH, segment_length + spacing):
        pygame.draw.line(screen, line_color, (x, start_y), (x + segment_length, start_y), 2)
