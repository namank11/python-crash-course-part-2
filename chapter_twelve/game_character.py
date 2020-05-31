import sys

import pygame


class GameCharacter:
    def __init__(self, blue_sky):
        self.screen = blue_sky.screen
        self.screen_rect = blue_sky.screen.get_rect()
        self.image = pygame.image.load('images/Download-Goku-PNG-File-172.bmp')
        self.rect = self.image.get_rect()
        self.rect.mid = self.screen_rect.mid

    def blitme(self):
        self.screen.blit(self.image, self.rect)