"""
A settings class for initializing all the setting attributes we will be using throughout the project
"""


class SidewaysShooterSettings:
    def __init__(self):

        # Game Screen Settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings

        self.ship_speed = 1.5

        # bullet settings

        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_speed = 1
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        self.fleet_speed = 10
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50
        self.speed_up_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0

