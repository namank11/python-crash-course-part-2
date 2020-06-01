import pygame

import sys

from steady_raindrop import SteadyRaindrop


class SteadyRainingWindow:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Rain Drops On Window")
        self.steady_raindrops = pygame.sprite.Group()
        self._create_droplets()

    def _create_droplets(self):
        steadyraindrop = SteadyRaindrop(self)
        steadyraindrop_width, steadyraindrop_height = steadyraindrop.rect.size
        available_space_horizontally = self.screen_width - (2 * steadyraindrop_width)
        number_drops_fit_horizontally = available_space_horizontally // (2 * steadyraindrop_width)
        for drops in range(number_drops_fit_horizontally):
            self._create_drop(drops)

    def _check_collision(self):
        flag = False
        screen_rect = self.screen.get_rect()
        for drop in self.steady_raindrops:
            if drop.rect.bottom >= screen_rect.bottom:
                self.steady_raindrops.remove(drop)
                flag = True
        if flag:
            return True
        else:
            return False

    def _create_drop(self, drops):
        steadyraindrop = SteadyRaindrop(self)
        steadyraindrop_width, steadyraindrop_height = steadyraindrop.rect.size
        steadyraindrop.x = steadyraindrop_width + 2 * steadyraindrop_width * drops
        steadyraindrop.rect.x = steadyraindrop.x
        self.steady_raindrops.add(steadyraindrop)


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.steady_raindrops.draw(self.screen)
            self.steady_raindrops.update()
            if self._check_collision():
                self._create_droplets()
            pygame.display.flip()


if __name__ == "__main__":
    steadyrainingwindow = SteadyRainingWindow()
    steadyrainingwindow.run_game()
