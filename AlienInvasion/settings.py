import pygame

class Settings:
    """a class to store all settings for alien invasion"""

    def __init__(self):
        """initialize the gal settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = pygame.image.load('space.bmp')

        # alien settings
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quicly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.3

        # fleet direction of 1 reprsaents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """increasn speed settings and alien value points"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

