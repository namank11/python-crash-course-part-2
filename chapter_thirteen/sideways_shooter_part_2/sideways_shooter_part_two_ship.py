import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/side_ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midright = self.screen_rect.midright
        self.yfloat = float(self.rect.y)

        self.moving_down = False
        self.moving_up = False

    def update_movement(self):

        # method for the movement of the ship

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.yfloat += self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.yfloat -= self.settings.ship_speed

        # updating the rect object from xfloat

        self.rect.y = self.yfloat

    def blitme(self):
        self.screen.blit(self.image, self.rect)