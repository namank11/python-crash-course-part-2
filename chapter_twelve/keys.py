import sys

import pygame


class Blank:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blank")
        self.bg_color = (0, 0, 0)

    def _event_keypressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print(event.key)
            elif event.key == pygame.K_LEFT:
                print(event.key)
            elif event.key == pygame.K_DOWN:
                print(event.key)
            elif event.key == pygame.K_UP:
                print(event.key)
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._event_keypressed(event)

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    b = Blank()
    b.run_game()
