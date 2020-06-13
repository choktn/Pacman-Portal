import pygame

from pygame.sprite import Sprite


class PortalBullet(Sprite):
    def __init__(self, settings, screen, pacman):
        super(PortalBullet, self).__init__()

        self.screen = screen
        self.settings = settings

        self.rect = pygame.Rect(0, 0,  15, 3)

        self.rect.x = pacman.rect.x + 16
        self.rect.y = pacman.rect.y + 16

        self.bullet_width = None
        self.bullet_height = None

        self.color = settings.bullet_color
        self.speed = settings.bullet_speed
        self.x = self.rect.x
        self.y = self.rect.y
        self.direction = "None"
        self.type = "portalbullet"
        self.colx = None
        self.coly = None

    def update_bullet(self, pacman):
        if self.direction == "None":
            if pacman.moving_up or pacman.facing == "up":
                self.direction = "up"
            elif pacman.moving_down or pacman.facing == "down":
                self.direction = "down"
            elif pacman.moving_left or pacman.facing == "left":
                self.direction = "left"
            elif pacman.moving_right or pacman.facing == "right":
                self.direction = "right"
        if self.direction != "None":
            if self.direction == "up":
                self.y -= self.speed
                self.rect.y = self.y
                self.bullet_width = 3
                self.bullet_height = 15
            elif self.direction == "down":
                self.y += self.speed
                self.rect.y = self.y
                self.bullet_width = 3
                self.bullet_height = 15
            elif self.direction == "left":
                self.x -= self.speed
                self.rect.x = self.x
                self.bullet_width = 15
                self.bullet_height = 3
            elif self.direction == "right":
                self.x += self.speed
                self.rect.x = self.x
                self.bullet_width = 15
                self.bullet_height = 3
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.bullet_width, self.bullet_height)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
