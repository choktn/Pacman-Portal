import pygame

from pygame.sprite import Sprite


class DrawGrid(Sprite):
    def __init__(self, screen):
        super(DrawGrid, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, 30, 30)

        self.outline = None
        self.color = None
        self.block_size = None
        self.type = None
        self.hascollided = None
        self.coordcount = -1

    def draw_block(self):
        pygame.draw.rect(self.screen, self.color, ((self.rect.x, self.rect.y), (self.block_size, self.block_size)),
                         self.outline)
