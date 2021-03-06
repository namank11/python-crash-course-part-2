import sys

import pygame

from sideways_shooter_settings import SidewaysShooterSettings

from sideways_shooter_ship import SidewaysShooterShip

from sideways_shooter_bullet import SidewaysShooterBullet


class SidewaysShooter:

    # Class for managing all the game assets and behaviour

    def __init__(self):

        # initializing Game and resources

        pygame.init()
        self.settings = SidewaysShooterSettings()
        pygame.display.set_caption("Sideways Shooter")
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.ship = SidewaysShooterShip (self)

        # making a group of bullets using the group class of the sprite module to update the bullets which
        # are already been fired

        self.bullets = pygame.sprite.Group()

    def _check_keyup_events(self, event):

        # defining what to do when down or up key is released

        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _check_keydown_event(self, event):

        # defining what to do when a up, down, space or q key is pressed

        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = SidewaysShooterBullet(self)
            self.bullets.add(new_bullet)

    def _check_events(self):

        # A Helper method to to reduce the size of the run_game method

        for event in pygame.event.get():

            # event loop for monitoring all the events occurring through out the running of the program

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                # monitoring when a key is pressed

                self._check_keydown_event(event)

            elif event.type == pygame.KEYUP:

                # monitoring when a key is released

                self._check_keyup_events(event)

    def _update_screen(self):

        # Another helper method for updating the changes occurring on the surface of the game

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _update_bullets(self):

        # calling the update method using the bullets group initialized in the __init__ method of this class

        self.bullets.update()

        # deleting the bullets which are out of the surface of the game

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().width:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def run_game(self):

        # essential method for managing all the game program

        while True:
            self._check_events()
            self.ship.update_movement()
            self._update_bullets()
            self._update_screen()


if __name__ == '__main__':

    # Driver Program

    ss = SidewaysShooter()
    ss.run_game()
