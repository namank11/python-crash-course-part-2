import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):

        # initializing all the attributes using the super class 'sprite'

        super().__init__()

        # initializing some more attributes which will be used for the bullets

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # setting the bullet properties at top left corner then placing the bullet at the ship's rectangle midtop

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):

        # updating the bullet position using the bullet speed from settings file

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):

        # drawing the bullet

        pygame.draw.rect(self.screen, self.color, self.rect)

