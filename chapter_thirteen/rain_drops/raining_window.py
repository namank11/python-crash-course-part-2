import pygame

import sys

from raindrop import Raindrop


class RainingWindow:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Rain Drops On Window")
        self.raindrops = pygame.sprite.Group()
        self._create_droplets()

    def _create_droplets(self):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_horizontally = self.screen_width - (2 * raindrop_width)
        number_drops_fit_horizontally = available_space_horizontally // (2 * raindrop_width)
        for drops in range(number_drops_fit_horizontally):
            self._create_drop(drops)

    def _create_drop(self, drops):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * drops
        raindrop.rect.x = raindrop.x
        self.raindrops.add(raindrop)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.raindrops.draw(self.screen)
            self.raindrops.update()
            pygame.display.flip()


if __name__ == "__main__":
    rainingwindow = RainingWindow()
    rainingwindow.run_game()
