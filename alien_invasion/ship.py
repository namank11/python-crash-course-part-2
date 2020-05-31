"""
A class define the ship attributes to be used in the game
"""

import pygame

from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_game):

        # initializing the ship and its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # loading the ship and setting it as a rec tangle

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # starting each new ship at the bottom of the game screen

        self.rect.midbottom = self.screen_rect.midbottom

        # initializing all the moving flags

        self.xfloat = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update_movement(self):

        # method for the movement of the ship

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.xfloat += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.xfloat -= self.settings.ship_speed

        # updating the rect object from xfloat

        self.rect.x = self.xfloat

    def _check_aliens_bottom(self):

        # check if any alien collides with the ground

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def center_ship(self):

        # placing the ship at the original position after the game restarts

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):

        # method for placing the ship at its defined position

        self.screen.blit(self.image, self.rect)
