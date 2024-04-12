import pygame

import constants


class Menu:
    def __init__(self, screen, exit_callback):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.is_show = True
        self.play_button = PlayButton(constants.SCREEN_WIDTH / 2, 100, 20, 20, 'Play', 'black', 'white')
        self.exit_button = ExitButton(constants.SCREEN_WIDTH / 2, 200, 20, 20, 'Exit', 'black', 'white')
        self.on_exit = exit_callback
        self.show_menu()

    def show_menu(self):
        print("show menu =", self.is_show)
        if self.is_show:
            self.screen.fill((0, 0, 0))
            self.play_button.draw(self.screen)
            self.exit_button.draw(self.screen)
            pygame.display.update()


class PlayButton:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 100)  # Choose font

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class ExitButton:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 100)  # Choose font

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
