import sys

import pygame

from settings import Settings

from ship import Ship

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

from alien import Alien

from time import sleep

from bullet import Bullet


class AlienInvasion:

    # Class for managing all the game assets and behaviour

    def __init__(self):

        # initializing Game and resources

        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)

        # adding the alien ship to the sprite group

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # making a group of bullets using the group class of the sprite module to update the bullets which
        # are already been fired

        self.bullets = pygame.sprite.Group()

        self.play_button = Button(self, "Play")

        self.score_board = Scoreboard(self)

    def _check_keyup_events(self, event):
        # defining what to do when right or left key is released

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_event(self, event):
        # defining what to do when a right, left or q key is pressed

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.stats.game_active = True
            self.score_board.prep_score()
            self.score_board.prep_level()
            self.score_board.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # calling the update method using the bullets group initialized in the __init__ method of this class

        self.bullets.update()

        # deleting the bullets which are out of the surface of the game

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.score_board.prep_score()
            self.score_board.prep_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increse_speed()

            self.stats.level += 1
            self.score_board.prep_level()

    def _create_fleet(self):
        # creating an instance of the alien class

        alien = Alien(self)

        # calculating how many aliens we can fit horizontally

        alien_width = alien.rect.width
        available_space_horizontally = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_horizontally = available_space_horizontally // (2 * alien_width)

        # calculating how many rows of aliens we can fit within our screen size and excluding the ship size

        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_vertically = self.settings.screen_height - (10 * alien_height) - ship_height
        number_of_aliens_vertically = available_space_vertically // (2 * alien_height)
        for rows in range(number_of_aliens_vertically):
            for alien_numbers in range(number_of_aliens_horizontally):
                self._create_alien(alien_numbers, rows)

    def _create_alien(self, alien_numbers, rows):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = alien.x
        alien.rect.x = alien.x = alien_width + 2 * alien_width * alien_numbers
        alien.rect.y = alien.rect.height + 2 * alien_height * rows
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge_collision():
                self._change_fleet_direction()

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.score_board.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        # Another helper method for updating the changes occurring on the surface of the game

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.score_board.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def run_game(self):

        # essential method for managing all the game program

        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update_movement()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()


if __name__ == '__main__':
    # Driver Program

    ai = AlienInvasion()
    ai.run_game()
