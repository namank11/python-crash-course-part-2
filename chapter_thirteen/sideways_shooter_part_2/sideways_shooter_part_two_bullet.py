import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # setting the bullet properties at top left corner then placing the bullet at the ship's rectangle midtop

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = ai_game.ship.rect.midleft
        self.x = float(self.rect.x)

    def update(self):
        # updating the bullet position using the bullet speed from settings file

        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        # drawing the bullet

        pygame.draw.rect(self.screen, self.color, self.rect)