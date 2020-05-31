import sys

import pygame

class Rocket:
    def __init__(self, space):

        # initializing the screen variables which is to be used in rocket class

        self.screen = space.screen
        self.screen_rect = space.screen.get_rect()

        # loading the ship.bmp and setting it on the pygame screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        # initializing all the moving flags

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_movement(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)