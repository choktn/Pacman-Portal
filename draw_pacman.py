import pygame

from pygame.sprite import Sprite


class DrawPacman(Sprite):
    def __init__(self, settings, screen):
        super(DrawPacman, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.transform.scale(pygame.image.load('images/pacmanmove1.png'), (33, 33))

        self.pacman_move1 = pygame.transform.scale(pygame.image.load('images/pacmanmove1.png'), (33, 33))
        self.pacman_move2 = pygame.transform.scale(pygame.image.load('images/pacmanmove2.png'), (33, 33))
        self.pacman_move3 = pygame.transform.scale(pygame.image.load('images/pacmanmove3.png'), (33, 33))
        self.pacman_move4 = pygame.transform.scale(pygame.image.load('images/pacmanmove4.png'), (33, 33))

        self.pacman_deathmove1 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove1.png'), (33, 33))
        self.pacman_deathmove2 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove2.png'), (33, 33))
        self.pacman_deathmove3 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove3.png'), (33, 33))
        self.pacman_deathmove4 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove4.png'), (33, 33))
        self.pacman_deathmove5 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove5.png'), (33, 33))
        self.pacman_deathmove6 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove6.png'), (33, 33))
        self.pacman_deathmove7 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove7.png'), (33, 33))
        self.pacman_deathmove8 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove8.png'), (33, 33))
        self.pacman_deathmove9 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove9.png'), (33, 33))
        self.pacman_deathmove10 = pygame.transform.scale(pygame.image.load('images/pacmandeathmove10.png'), (33, 33))
        self.pacman_deathmove11 = pygame.image.load('images/pacmandeathmove11.png')
        self.pacman_deathmove12 = pygame.image.load('images/pacmandeathmove12.png')
        self.pacman_deathmove13 = pygame.image.load('images/pacmandeathmove13.png')
        self.pacman_deathmove14 = pygame.image.load('images/pacmandeathmove14.png')
        self.pacman_deathmove15 = pygame.image.load('images/pacmandeathmove15.png')
        self.pacman_deathmove16 = pygame.image.load('images/pacmandeathmove16.png')

        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_right_q = False
        self.moving_left_q = False
        self.moving_up_q = False
        self.moving_down_q = False
        self.moving = False
        self.facing = "right"
        self.destruct = False
        self.death_framecount = 0

        self.type = "pacman"

    def draw_pacman(self, blocks):
        for block in blocks.sprites():
            if block.type == "start":
                self.x = block.rect.x - 13
                self.y = block.rect.y - 16
                break

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
