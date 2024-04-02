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
        self.player_score = 0
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

        if self.top <= 0 or self.bottom >= constants.SCREEN_HEIGHT:
            self.restart()
        if self.left <= 0 or self.right >= constants.SCREEN_WIDTH:
            self.x_speed *= -1

    def restart(self):
        self.x = self.x_spawn
        self.y = self.y_spawn

    def draw(self):
        pygame.draw.ellipse(self.screen, 'gray', self)


def draw_dotted_line(surface, color, start_pos, end_pos, segment_length=5, spacing=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx, dy = x2 - x1, y2 - y1  # Calculate direction vector
    distance = max(abs(dx), abs(dy))  # Approximate distance

    for i in range(0, distance, segment_length + spacing):
        if i < distance:  # Check if within visible segment range
            x, y = x1 + (dx * i) / distance, y1 + (dy * i) / distance
            pygame.draw.line(surface, color, (x, y), (x + segment_length, y + segment_length), 1)