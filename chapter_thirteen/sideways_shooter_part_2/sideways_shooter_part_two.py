import pygame

import sys

from sideways_shooter_part_two_settings import Settings

from sideways_shooter_part_two_ship import Ship

from sideways_shooter_part_two_bullet import Bullet

from sideways_shooter_part_two_alien import Alien


class SidewaysShooterPartTwo:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption("Sideways Shooter 2")

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # calling the update method using the bullets group initialized in the __init__ method of this class

        self.bullets.update()

        # deleting the bullets which are out of the surface of the game

        for bullet in self.bullets.copy():
            if bullet.rect.left <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _create_fleet(self):
        # creating an instance of the alien class

        alien = Alien(self)

        # calculating how many aliens we can fit horizontally

        alien_width = alien.rect.width
        available_space_horizontally = self.settings.screen_width - (10 * alien_width)
        number_of_aliens_horizontally = available_space_horizontally // (2 * alien_width)

        # calculating how many rows of aliens we can fit within our screen size and excluding the ship size

        alien_width, alien_height = alien.rect.size
        available_space_vertically = self.settings.screen_height + (4 * alien_height)
        number_of_aliens_vertically = available_space_vertically // (2 * alien_height)
        for rows in range(number_of_aliens_vertically):
            for alien_numbers in range(number_of_aliens_horizontally):
                self._create_alien(alien_numbers, rows)

    def _create_alien(self, alien_numbers, rows):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = alien_width + 2 * alien_width * alien_numbers
        alien.rect.y = alien.y = alien.rect.height + 2 * alien_height * rows
        self.aliens.add(alien)

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x += self.settings.fleet_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge_collision():
                self._change_fleet_direction()

    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _key_pressed(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _key_released(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_pressed(event)
            elif event.type == pygame.KEYUP:
                self._key_released(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship Destroyed!")
            self.settings.ships_left -= self.settings.ships_left
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
        self.ship.update_movement()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self._update_bullets()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


if __name__ == "__main__":
    sidewaysshooterparttwo = SidewaysShooterPartTwo()
    sidewaysshooterparttwo.run_game()
