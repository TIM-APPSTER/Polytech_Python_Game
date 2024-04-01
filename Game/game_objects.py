import pygame

import constants


class PlayerRackets:
    def __init__(self, screen):
        self.x = constants.SCREEN_WIDTH / 2 - 25  # Initial x position
        self.y = constants.SCREEN_HEIGHT - 25  # Fixed y position
        self.speed = 2
        self.player_score = 0
        self.screen = screen
        self.player = pygame.Rect(self.x, self.y, 50, 5)  # Use self.x and self.y

    def move(self, dt):  # Pass dt as an argument
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.player.x += self.speed * dt

        if self.player.left <= 0:
            self.player.left = 0
        if self.player.right >= constants.SCREEN_WIDTH:
            self.player.right = constants.SCREEN_WIDTH

    def draw(self):
        pygame.draw.rect(self.screen, 'gray', self.player)
