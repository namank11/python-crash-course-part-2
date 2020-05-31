import sys

import pygame

from star import Star

from random import randint

class BetterStars:
    def __init__(self):
        pygame.init()

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Sky Full Of Stars')

        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_row = available_space_x // (2 * star_width)
        available_space_y = self.screen_height - (2 * star_height)
        number_stars_column = available_space_y // (2 * star_height)
        random_row = randint(0, number_stars_column)
        random_number = randint(0, number_stars_row)
        for rows in range(number_stars_column):
            for star_number in range(number_stars_row):
                self._create_star(random_number, random_row)

    def _create_star(self, random_number, random_row):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * random_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * random_row
        self.stars.add(star)

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    betterstars = BetterStars()
    betterstars.run_game()
