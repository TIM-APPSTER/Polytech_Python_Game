import pygame

import constants


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.is_show = True
        self.play_button = Button(self.screen, 'Play', 300, 150, 100, 100, 'white', 'black', None)
        self.exit_button = Button(self.screen, 'Exit', 300, 300, 200, 200, 'white', 'black', None)
        self.screen_surf = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.show_menu()

    def show_menu(self):
        self.screen_surf.fill('black')
        self.screen_surf.set_alpha(150)
        self.screen.blit(self.screen_surf, (0, 0))
        self.play_button.draw_button()
        self.exit_button.draw_button()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.collidepoint(event.pos):
                    self.is_show = False

                if self.exit_button.collidepoint(event.pos):
                    exit()
        pygame.display.flip()


class Button(pygame.Rect):
    def __init__(self, screen, text, x, y, width, height, color, hover_color, font):
        super().__init__(x,y, width, height)
        self.screen = screen
        self.button_text = text
        self.text_color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font('Materials/Roboto-Black.ttf', 36)

    def draw_button(self):
        pygame.draw.rect(self.screen, self.hover_color, self)
        text_surface = self.font.render(self.button_text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.center)
        self.screen.blit(text_surface, text_rect)
