"""
A settings class for initializing all the setting attributes we will be using throughout the project
"""


class Settings:
    def __init__(self):

        # Game Screen Settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings

        self.ship_limit = 3

        # bullet settings

        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # alien settings

        # alien fleet settings

        self.fleet_speed = 10

        self.speed_up_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increse_speed(self):
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)