import json


class GameStats:
    """track statistics fos alien invasion"""

    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # start alien invasion in an active state
        self.game_active = False
        
        # high score should never be reset
        filename = 'highscore.json'
        with open(filename) as f:
            self.high_score = json.load(f)

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
