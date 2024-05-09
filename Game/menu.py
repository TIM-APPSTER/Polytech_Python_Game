import pygame

import constants


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.is_show = True
        self.play_button = Button(self.screen, 'Play', constants.SCREEN_WIDTH / 2, 150, 100, 100, 'white', 'right')
        self.exit_button = Button(self.screen, 'Exit', constants.SCREEN_WIDTH / 2, 300, 200, 200, 'white', 'center')
        self.screen_surf = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.show_menu()

    def show_menu(self):
        self.screen_surf.fill('black')
        self.screen_surf.set_alpha(150)
        self.screen.blit(self.screen_surf, (0, 0))
        self.play_button.draw_button()
        self.exit_button.draw_button()
        while self.is_show:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.collidepoint(event.pos):
                        self.is_show = False
                    if self.exit_button.collidepoint(event.pos):
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_show = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LALT and event.key == pygame.K_F4:
                        exit()
            pygame.display.flip()


class Button(pygame.Rect):
    def __init__(self, screen, text, x, y, width, height, color, placement):
        super().__init__(x, y, width, height)
        self.screen = screen
        self.button_text = text
        self.text_color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font('Game/Materials/fonts/Roboto-Black.ttf', 36)

    def draw_button(self):
        # pygame.draw.rect(self.screen, self.text_color, self)
        text_surface = self.font.render(self.button_text, True, self.text_color)
        text_rect = text_surface.get_rect()
        if self.placement == 'center':
            text_rect.center = self.center
        elif self.placement == 'left':
            text_rect.midleft = self.midleft
        elif self.placement == 'right':
            text_rect.midright = self.midright
        self.screen.blit(text_surface, text_rect)
