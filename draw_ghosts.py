import pygame

from pygame.sprite import Sprite


class DrawGhosts(Sprite):
    def __init__(self, settings, screen, num):
        super(DrawGhosts, self).__init__()
        self.screen = screen
        self.settings = settings
        self.blinky = pygame.transform.smoothscale(pygame.image.load('images/blinkyupmove1.png'), (33, 33))
        self.pinky = pygame.transform.smoothscale(pygame.image.load('images/pinkyupmove1.png'), (33, 33))
        self.clyde = pygame.transform.smoothscale(pygame.image.load('images/clydeupmove1.png'), (33, 33))
        self.inkey = pygame.transform.smoothscale(pygame.image.load('images/inkeyupmove1.png'), (33, 33))

        self.blinkyup1 = pygame.transform.smoothscale(pygame.image.load('images/blinkyupmove1.png'), (33, 33))
        self.blinkyup2 = pygame.transform.smoothscale(pygame.image.load('images/blinkyupmove2.png'), (33, 33))
        self.blinkyright1 = pygame.transform.smoothscale(pygame.image.load('images/blinkyrightmove1.png'), (33, 33))
        self.blinkyright2 = pygame.transform.smoothscale(pygame.image.load('images/blinkyrightmove2.png'), (33, 33))
        self.blinkyleft1 = pygame.transform.smoothscale(pygame.image.load('images/blinkyleftmove1.png'), (33, 33))
        self.blinkyleft2 = pygame.transform.smoothscale(pygame.image.load('images/blinkyleftmove2.png'), (33, 33))
        self.blinkydown1 = pygame.transform.smoothscale(pygame.image.load('images/blinkydownmove1.png'), (33, 33))
        self.blinkydown2 = pygame.transform.smoothscale(pygame.image.load('images/blinkydownmove2.png'), (33, 33))

        self.clydeup1 = pygame.transform.smoothscale(pygame.image.load('images/clydeupmove1.png'), (33, 33))
        self.clydeup2 = pygame.transform.smoothscale(pygame.image.load('images/clydeupmove2.png'), (33, 33))
        self.clyderight1 = pygame.transform.smoothscale(pygame.image.load('images/clyderightmove1.png'), (33, 33))
        self.clyderight2 = pygame.transform.smoothscale(pygame.image.load('images/clyderightmove2.png'), (33, 33))
        self.clydeleft1 = pygame.transform.smoothscale(pygame.image.load('images/clydeleftmove1.png'), (33, 33))
        self.clydeleft2 = pygame.transform.smoothscale(pygame.image.load('images/clydeleftmove2.png'), (33, 33))
        self.clydedown1 = pygame.transform.smoothscale(pygame.image.load('images/clydedownmove1.png'), (33, 33))
        self.clydedown2 = pygame.transform.smoothscale(pygame.image.load('images/clydedownmove2.png'), (33, 33))

        self.pinkyup1 = pygame.transform.smoothscale(pygame.image.load('images/pinkyupmove1.png'), (33, 33))
        self.pinkyup2 = pygame.transform.smoothscale(pygame.image.load('images/pinkyupmove2.png'), (33, 33))
        self.pinkyright1 = pygame.transform.smoothscale(pygame.image.load('images/pinkyrightmove1.png'), (33, 33))
        self.pinkyright2 = pygame.transform.smoothscale(pygame.image.load('images/pinkyrightmove2.png'), (33, 33))
        self.pinkyleft1 = pygame.transform.smoothscale(pygame.image.load('images/pinkyleftmove1.png'), (33, 33))
        self.pinkyleft2 = pygame.transform.smoothscale(pygame.image.load('images/pinkyleftmove2.png'), (33, 33))
        self.pinkydown1 = pygame.transform.smoothscale(pygame.image.load('images/pinkydownmove1.png'), (33, 33))
        self.pinkydown2 = pygame.transform.smoothscale(pygame.image.load('images/pinkydownmove2.png'), (33, 33))

        self.inkeyup1 = pygame.transform.smoothscale(pygame.image.load('images/inkeyupmove1.png'), (33, 33))
        self.inkeyup2 = pygame.transform.smoothscale(pygame.image.load('images/inkeyupmove2.png'), (33, 33))
        self.inkeyright1 = pygame.transform.smoothscale(pygame.image.load('images/inkeyrightmove1.png'), (33, 33))
        self.inkeyright2 = pygame.transform.smoothscale(pygame.image.load('images/inkeyrightmove2.png'), (33, 33))
        self.inkeyleft1 = pygame.transform.smoothscale(pygame.image.load('images/inkeyleftmove1.png'), (33, 33))
        self.inkeyleft2 = pygame.transform.smoothscale(pygame.image.load('images/inkeyleftmove2.png'), (33, 33))
        self.inkeydown1 = pygame.transform.smoothscale(pygame.image.load('images/inkeydownmove1.png'), (33, 33))
        self.inkeydown2 = pygame.transform.smoothscale(pygame.image.load('images/inkeydownmove2.png'), (33, 33))

        self.ghostrun1 = pygame.transform.smoothscale(pygame.image.load('images/ghostrunmove1.png'), (33, 33))
        self.ghostrun2 = pygame.transform.smoothscale(pygame.image.load('images/ghostrunmove2.png'), (33, 33))
        self.ghost2run1 = pygame.transform.smoothscale(pygame.image.load('images/ghostrun2move1.png'), (33, 33))
        self.ghost2run2 = pygame.transform.smoothscale(pygame.image.load('images/ghostrun2move2.png'), (33, 33))

        if num == 1:
            self.image = self.blinky
            self.type = "blinky"
        elif num == 2:
            self.image = self.pinky
            self.type = "pinky"
        elif num == 3:
            self.image = self.clyde
            self.type = "clyde"
        elif num == 4:
            self.image = self.inkey
            self.type = "inkey"
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.shouldmove_right = False
        self.shouldmove_left = False
        self.shouldmove_up = False
        self.shouldmove_down = False
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.force_ghost = False
        self.run = False
        self.runhit = False
        self.mode = ""

    def draw_ghost(self):
        self.screen.blit(self.image, self.rect)
