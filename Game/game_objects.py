import random

import pygame

import constants


class Racket:
    def __init__(self, screen, x, y, left_key, right_key):
        self.x = x
        self.y = y
        self.left_key = left_key
        self.right_key = right_key
        self.speed = 2
        self.dt = 5
        self.player_score = 0
        self.screen = screen
        self.player = pygame.Rect(self.x, self.y, 50, 5)  # Use self.x and self.y

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.left_key]:
            self.player.x -= self.speed * self.dt
        if keys[self.right_key]:
            self.player.x += self.speed * self.dt

        if self.player.left <= 0:
            self.player.left = 0
        if self.player.right >= constants.SCREEN_WIDTH:
            self.player.right = constants.SCREEN_WIDTH

    def draw(self):
        pygame.draw.rect(self.screen, 'gray', self.player)


class Ball:
    def __init__(self, screen):
        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 2
        self.radius = 5
        self.x_speed = 5
        self.y_speed = 5
        self.dt = 5
        self.screen = screen
        self.ball = pygame.Rect(self.x, self.y, 50, 5)

    def move(self):
        self.ball.x += self.x_speed
        self.ball.y += self.y_speed

        if self.ball.top <= 0 or self.ball.bottom >= constants.SCREEN_HEIGHT:
            self.y_speed *= -1
        if self.ball.left <= 0 or self.ball.right >= constants.SCREEN_WIDTH:
            self.x_speed *= -1



            # Retro effect: Simulate slowdown and speedup
        if random.random() < 0.01:  # 1% chance to change speed
            self.x_speed *= random.choice([-1, 1])  # Randomly reverse or maintain direction
            self.y_speed *= random.choice([-1, 1])


    def draw(self):
        pygame.draw.circle(self.screen, 'gray', (self.x, self.y), self.radius)
