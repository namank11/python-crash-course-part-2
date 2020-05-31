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

