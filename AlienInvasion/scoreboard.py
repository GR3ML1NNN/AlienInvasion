import pygame.font
from pygame.sprite import Group
from ship import Ship
import json

class ScoreBoard:
    """a class to report scroringt information"""

    def __init__(self, ai_game):
        """initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings ofor scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        """turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color)
                
        # display the store at hte top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ship_lives, self.ship_lives_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "high score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                 self.text_color)
        
        # cente the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        filename = 'highscore.json'
        with open(filename, 'w') as f:
            json.dump(high_score, f)

    def check_high_score(self):
        """check to see if theres a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = "lv: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                 self.text_color)
        
        # position it below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''show how many ships are left'''
        ship_str = "lives: "
        self.ship_lives = self.font.render(ship_str, True, self.text_color)
        self.ship_lives_rect = self.ship_lives.get_rect()
        self.ship_lives_rect.left = self.screen_rect.left + 10
        self.ship_lives_rect.y += 10
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = self.ship_lives_rect.right + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
