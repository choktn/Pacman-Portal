import pygame

from pygame.sprite import Group
from draw_pacman import DrawPacman


class Scoreboard:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings

        self.font = pygame.font.SysFont(None, 40)
        self.lives = None

    def update_lives(self):
        self.lives = Group()
        for live in range(self.settings.paclives):
            pacman = DrawPacman(self.settings, self.screen)
            pacman.rect.x = (10 + live * pacman.rect.width) + 380
            pacman.rect.y = 700
            self.lives.add(pacman)

    def update_scoreboard(self):
        scoretext = self.font.render("Score: " + str(self.settings.score), False, (255, 255, 255))
        livestext = self.font.render("Lives: ", False, (255, 255, 255))
        self.screen.blit(scoretext, (50, 700))
        self.screen.blit(livestext, (300, 700))
        self.lives.draw(self.screen)
