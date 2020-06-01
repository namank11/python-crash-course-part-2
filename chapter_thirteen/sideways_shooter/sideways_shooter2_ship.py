"""
A class define the ship attributes to be used in the game
"""

import pygame


class SidewaysShooterShip:

    def __init__(self, ai_game):

        # initializing the screen and its rectangle

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # loading the ship and setting it as a rec tangle

        self.image = pygame.image.load('images/side_ship.bmp')
        self.rect = self.image.get_rect()

        # starting each new ship at the left of the game screen

        self.rect.midleft = self.screen_rect.midleft

        # initializing all the moving flags

        self.yfloat = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update_movement(self):

        # method for the movement of the ship

        if self.moving_up and self.rect.top > 0:
            self.yfloat -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.yfloat += self.settings.ship_speed

        # updating the rect object from yfloat

        self.rect.y = self.yfloat

    def blitme(self):

        # method for placing the ship at its defined position

        self.screen.blit(self.image, self.rect)
