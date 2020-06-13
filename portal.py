import pygame

from pygame.sprite import Sprite


class Portal(Sprite):
    def __init__(self, screen, num):
        super(Portal, self).__init__()
        self.screen = screen

        if num == 1:
            self.image = pygame.transform.scale(pygame.image.load('images/portal1.png'), (33, 33))
            self.rect = self.image.get_rect()
            self.type = "portal1"
        elif num == 2:
            self.image = pygame.transform.scale(pygame.image.load('images/portal2.png'), (33, 33))
            self.rect = self.image.get_rect()
            self.type = "portal2"
        self.x = self.rect.x
        self.y = self.rect.y

    def draw_portal(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
