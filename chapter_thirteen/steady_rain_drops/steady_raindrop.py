import pygame

from pygame.sprite import Sprite


class SteadyRaindrop(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/transparent-raindrops-2-original.bmp")
        self.rect = self.image.get_rect()
        self.drop_speed = 1
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):

        self.y += self.drop_speed
        self.rect.y = self.y
