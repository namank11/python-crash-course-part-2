"""
A class for managing the different state of the game
"""


class GameStats:

    def __init__(self, ai_game):

        self.ai_settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.game_active = False

    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.ships_left = self.ai_settings.ship_limit