import sys

import pygame

from rocket import Rocket

class Space:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket in Space")
        self.bg_color = (0, 0, 0)
        self.rocket = Rocket(self)

    def _event_keypressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.rocket.moving_left = True
            elif event.key == pygame.K_DOWN:
                self.rocket.moving_down = True
            elif event.key == pygame.K_UP:
                self.rocket.moving_up = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

    def _event_keyreleased(self, event):

        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    self._event_keyreleased(event)
                elif event.type == pygame.KEYDOWN:
                    self._event_keypressed(event)
            self.screen.fill(self.bg_color)
            self.rocket.update_movement()
            self.rocket.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    s = Space()
    s.run_game()
