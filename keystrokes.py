import pygame
import sys
import create_objects

from portal_bullet import PortalBullet
from fruits import Fruit


def check_keydown_events(event, pacman, portal_bullet, screen, settings):
    if event.key == pygame.K_RIGHT:
        if pacman.moving and not pacman.moving_right:
            pacman.moving_right_q = True
            pacman.moving_left_q = False
            pacman.moving_down_q = False
            pacman.moving_up_q = False
        else:
            pacman.moving_right = True
            pacman.moving = True
            pacman.moving_left = False
            pacman.moving_down = False
            pacman.moving_up = False
    elif event.key == pygame.K_LEFT:
        if pacman.moving and not pacman.moving_left:
            pacman.moving_right_q = False
            pacman.moving_left_q = True
            pacman.moving_down_q = False
            pacman.moving_up_q = False
        else:
            pacman.moving_left = True
            pacman.moving = True
            pacman.moving_right = False
            pacman.moving_down = False
            pacman.moving_up = False
    elif event.key == pygame.K_DOWN:
        if pacman.moving and not pacman.moving_down:
            pacman.moving_right_q = False
            pacman.moving_left_q = False
            pacman.moving_down_q = True
            pacman.moving_up_q = False
        else:
            pacman.moving_down = True
            pacman.moving = True
            pacman.moving_up = False
            pacman.moving_left = False
            pacman.moving_right = False
    elif event.key == pygame.K_UP:
        if pacman.moving and not pacman.moving_up:
            pacman.moving_right_q = False
            pacman.moving_left_q = False
            pacman.moving_down_q = False
            pacman.moving_up_q = True
        else:
            pacman.moving_up = True
            pacman.moving = True
            pacman.moving_down = False
            pacman.moving_left = False
            pacman.moving_right = False
    elif event.key == pygame.K_SPACE:
        if settings.active_portals != 2:
            new_portal = PortalBullet(settings, screen, pacman)
            portal_bullet.add(new_portal)
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(event, pacman, portal_bullet,  screen, settings, ghosts, blocks, fruits, play_button, highscore_button,
                 back_button):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        check_keydown_events(event, pacman, portal_bullet, screen, settings)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        check_play_button(settings, screen, pacman, ghosts, blocks, fruits, play_button, mouse_x, mouse_y)
        check_highscore_button(highscore_button, settings, mouse_x, mouse_y)
        check_back_button(back_button, settings, mouse_x, mouse_y)


def check_play_button(settings, screen, pacman, ghosts, blocks, fruits, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not settings.playing:
        settings.titlescreen_active = False
        settings.playing = True
        settings.resettitleanimation = True
        for block in blocks.sprites():
            blocks.remove(block)
        for ghost in ghosts.sprites():
            ghosts.remove(ghost)
        for fruit in fruits.sprites():
            fruits.remove(fruit)
        create_objects.create_grid(settings, screen, blocks)
        create_objects.create_ghosts(settings, screen, ghosts, blocks, "all")

        pacman.draw_pacman(blocks)
        pacman.moving = False
        pacman.moving_right = False
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = False

        scoreboardfruit = Fruit(screen, 1)
        fruits.add(scoreboardfruit)
        scoreboardfruit.x = 650
        scoreboardfruit.y = 700


def check_highscore_button(highscore_button, settings, mouse_x, mouse_y):
    button_clicked = highscore_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not settings.playing:
        settings.titlescreen_active = False
        settings.highscorescreen_active = True
        settings.resettitleanimation = True


def check_back_button(back_button, settings, mouse_x, mouse_y):
    back_button_clicked = back_button.rect.collidepoint(mouse_x, mouse_y)
    if settings.highscorescreen_active:
        if back_button_clicked and not settings.playing:
            settings.highscorescreen_active = False
            settings.titlescreen_active = True
