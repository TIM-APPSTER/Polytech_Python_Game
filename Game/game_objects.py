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


class DrawScore:
    def __init__(self, screen, font_path, font_size, color=(255, 255, 255)):
        self.screen = screen
        self.font = pygame.font.Font(font_path, font_size)
        self.color = color

    def draw(self, score, x, y):
        score_text = self.font.render(str(score), True, self.color)
        score_rect = score_text.get_rect(topleft=(x, y))
        self.screen.blit(score_text, score_rect)


def draw_dotted_line(screen, line_color):
    start_x, start_y = (0, constants.SCREEN_HEIGHT / 2)
    segment_length = 5
    spacing = 10
    for x in range(start_x, constants.SCREEN_WIDTH, segment_length + spacing):
        pygame.draw.line(screen, line_color, (x, start_y), (x + segment_length, start_y), 2)