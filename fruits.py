import pygame

from pygame.sprite import Sprite


class Fruit(Sprite):
    def __init__(self, screen, num):
        super(Fruit, self).__init__()
        self.screen = screen
        self.width = 33
        self.height = 33
        if num == 1:
            self.image = pygame.transform.scale(pygame.image.load('images/cherry.png'), (self.width, self.height))
            self.rect = self.image.get_rect()
            self.type = "cherry"
            self.value = 100
        elif num == 2:
            self.image = pygame.transform.scale(pygame.image.load('images/strawberry.png'), (self.width, self.height))
            self.rect = self.image.get_rect()
            self.type = "strawberry"
            self.value = 300
        elif num == 3:
            self.image = pygame.transform.scale(pygame.image.load('images/orange.png'), (self.width, self.height))
            self.rect = self.image.get_rect()
            self.type = "orange"
            self.value = 500
        elif num == 4:
            self.image = pygame.transform.scale(pygame.image.load('images/apple.png'), (self.width, self.height))
            self.rect = self.image.get_rect()
            self.type = "apple"
            self.value = 700
        elif num == 5:
            self.image = pygame.transform.scale(pygame.image.load('images/melon.png'), (self.width, self.height))
            self.rect = self.image.get_rect()
            self.type = "melon"
            self.value = 1000
        elif num == 6:
            self.image = pygame.transform.scale(pygame.image.load('images/galaxianboss.png'), (self.width, self.height))
            self.rect = self.image.get_rect()
            self.type = "galaxianboss"
            self.value = 2000
        elif num == 7:
            self.image = pygame.transform.scale(pygame.image.load('images/bell.png'), (self.width, self.height))
            self.rect = self.image.get_rect()
            self.type = "bell"
            self.value = 3000
        elif num == 8:
            self.image = pygame.transform.scale(pygame.image.load('images/key.png'), (self.width, self.height))
            self.rect = self.image.get_rect()
            self.type = "key"
            self.value = 5000

        self.x = self.rect.x
        self.y = self.rect.y

    def draw_fruit(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
