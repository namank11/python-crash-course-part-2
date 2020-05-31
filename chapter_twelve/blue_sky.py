import sys

import pygame

from game_character import GameCharacter


class BlueSky:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (0, 0, 230)
        self.game_character = GameCharacter(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.game_character.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
