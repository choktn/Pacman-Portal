import pygame


class Settings:
    def __init__(self):
        self.screen_width = 810
        self.screen_height = 765
        self.bg_color = (0, 0, 0)

        self.playing = False

        self.pacspeed = 2
        self.paclives = 3
        self.score = 0
        self.dotcount = 0
        self.ghostspeed = 1
        self.ghostseaten = 1

        self.current_level = 1
        self.fruit_created = False
        self.timer = 0
        self.gamestarttimer = 0
        self.ghostsrunning = False

        self.bullet_color = (255, 255, 255)
        self.bullet_speed = 3
        self.active_portals = 0
        self.portal_passed = False

        self.titlescreen_active = True
        self.highscorescreen_active = False
        self.resettitleanimation = False
        self.beginningmusicplayed = False
        self.ambientghostplayed = False
        self.ghostrunningplayed = False
        self.disable_keystrokes = False

        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)
        self.channel3 = pygame.mixer.Channel(2)
