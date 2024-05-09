import pygame

import constants


class Racket(pygame.Rect):
    def __init__(self, screen: pygame.display.set_mode, x: int, y: int, left_key, right_key):
        super().__init__(x, y, 50, 5)
        self.x_spawn = x
        self.y_spawn = y
        self.left_key = left_key
        self.right_key = right_key
        self.speed = constants.RACKET_SPEED
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
    def __init__(self, screen):
        self.x_spawn = constants.SCREEN_WIDTH / 2
        self.y_spawn = constants.SCREEN_HEIGHT / 2
        super().__init__(self.x_spawn, self.y_spawn, 10, 10)
        self.radius = 5
        self.x_speed = constants.BALL_SPEED
        self.y_speed = constants.BALL_SPEED
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
        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 2
        self.countdown()

    def countdown(self):
        pass

    def draw(self):
        pygame.draw.ellipse(self.screen, 'gray', self)


def draw_dotted_line(screen, line_color):
    start_x, start_y = (0, constants.SCREEN_HEIGHT / 2)
    segment_length = 5
    spacing = 10
    for x in range(start_x, constants.SCREEN_WIDTH, segment_length + spacing):
        pygame.draw.line(screen, line_color, (x, start_y), (x + segment_length, start_y), 2)


def draw_countdown(screen, score_time):
    pygame.init()
    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - score_time

    if time_elapsed < 700:
        number = 3
    elif time_elapsed < 1400:
        number = 2
    elif time_elapsed < 2100:
        number = 1
    else:
        return  # Countdown finished

    countdown_text = constants.BASIC_FONT.render(str(number), True, 'white', 'black')
    text_rect = countdown_text.get_rect()
    text_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    screen.blit(countdown_text, text_rect)
