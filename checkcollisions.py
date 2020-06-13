import pygame

from miscellaneous import livelost
from portal import Portal
from time import sleep


def checkregularpacwall(settings, pacman, blocks):
    if pacman.moving_right:
        pacman.x += settings.pacspeed
        pacman.rect.x = pacman.x
        pacman.facing = "right"
    elif pacman.moving_left:
        pacman.x -= settings.pacspeed
        pacman.rect.x = pacman.x
        pacman.facing = "left"
    elif pacman.moving_down:
        pacman.y += settings.pacspeed
        pacman.rect.y = pacman.y
        pacman.facing = "down"
    elif pacman.moving_up:
        pacman.y -= settings.pacspeed
        pacman.rect.y = pacman.y
        pacman.facing = "up"

    if checkobjectwallcollisions(pacman, blocks, settings):
        if pacman.moving_right:
            pacman.x -= settings.pacspeed
            pacman.rect.x = pacman.x
            pacman.moving_right = False
        elif pacman.moving_left:
            pacman.x += settings.pacspeed
            pacman.rect.x = pacman.x
            pacman.moving_left = False
        if pacman.moving_down:
            pacman.y -= settings.pacspeed
            pacman.rect.y = pacman.y
            pacman.moving_down = False
        elif pacman.moving_up:
            pacman.y += settings.pacspeed
            pacman.rect.y = pacman.y
            pacman.moving_up = False
        pacman.moving = False


def checkqueuepacwall(settings, pacman, blocks):
    if pacman.moving_right_q:
        pacman.x += settings.pacspeed
        pacman.rect.x = pacman.x
    elif pacman.moving_left_q:
        pacman.x -= settings.pacspeed
        pacman.rect.x = pacman.x
    elif pacman.moving_down_q:
        pacman.y += settings.pacspeed
        pacman.rect.y = pacman.y
    elif pacman.moving_up_q:
        pacman.y -= settings.pacspeed
        pacman.rect.y = pacman.y

    if checkobjectwallcollisions(pacman, blocks, settings):
        if pacman.moving_right_q:
            pacman.x -= settings.pacspeed
            pacman.rect.x = pacman.x
        elif pacman.moving_left_q:
            pacman.x += settings.pacspeed
            pacman.rect.x = pacman.x
        elif pacman.moving_down_q:
            pacman.y -= settings.pacspeed
            pacman.rect.y = pacman.y
        elif pacman.moving_up_q:
            pacman.y += settings.pacspeed
            pacman.rect.y = pacman.y
    else:
        if pacman.moving_right_q:
            pacman.moving_right_q = False
            pacman.moving_right = True
            pacman.moving_left = False
            pacman.moving_down = False
            pacman.moving_up = False
        elif pacman.moving_left_q:
            pacman.moving_left = True
            pacman.moving_right = False
            pacman.moving_left_q = False
            pacman.moving_down = False
            pacman.moving_up = False
        elif pacman.moving_up_q:
            pacman.moving_right = False
            pacman.moving_left = False
            pacman.moving_down = False
            pacman.moving_up_q = False
            pacman.moving_up = True
        elif pacman.moving_down_q:
            pacman.moving_right = False
            pacman.moving_left = False
            pacman.moving_down_q = False
            pacman.moving_down = True
            pacman.moving_up = False


def checkpacmanportals(settings, screen, blocks, portals, portal_bullet):
    if settings.portal_passed:
        for portal in portals.sprites():
            portals.remove(portal)
        settings.active_portals = 0
        settings.portal_passed = False
    for bullet in portal_bullet.sprites():
        if checkobjectwallcollisions(bullet, blocks, settings):
            settings.active_portals += 1
            if settings.active_portals != 3:
                portal = None
                if settings.active_portals == 1:
                    portal = Portal(screen, 1)
                    portal.draw_portal(bullet.colx - 3, bullet.coly - 3)
                elif settings.active_portals == 2:
                    portal = Portal(screen, 2)
                    portal.draw_portal(bullet.colx - 3, bullet.coly - 3)
                for block in blocks.sprites():
                    if (portal.rect.x + 3) == block.rect.x and (portal.rect.y + 3) == block.rect.y:
                        if settings.active_portals == 1:
                            block.type = "blockp1"
                        elif settings.active_portals == 2:
                            block.type = "blockp2"
                portal_bullet.remove(bullet)
                portals.add(portal)
            else:
                settings.active_portals -= 1


def checkfruitpacmancollisions(settings, pacman, fruits):
    for fruit in fruits.sprites():
        if pygame.sprite.collide_rect(pacman, fruit):
            pygame.mixer.music.load('sounds/pacman_eatfruit.wav')
            pygame.mixer.music.play(1)
            settings.score += fruit.value
            fruits.remove(fruit)
            settings.dotcount -= 1
            break


def checktunnelpacmancollisions(settings, pacman, blocks):
    for block in blocks.sprites():
        if pygame.sprite.collide_rect(pacman, block):
            if block.type == "tunnel1":
                for tunnel in blocks.sprites():
                    if tunnel.type == "tunnel2":
                        pacman.x = tunnel.rect.x - 33
                        pacman.y = tunnel.rect.y - 16
                        pacman.rect.x = pacman.x
                        pacman.rect.y = pacman.y
            elif block.type == "tunnel2":
                for tunnel in blocks.sprites():
                    if tunnel.type == "tunnel1":
                        pacman.x = tunnel.rect.x + 33
                        pacman.y = tunnel.rect.y - 16
                        pacman.rect.x = pacman.x
                        pacman.rect.y = pacman.y
            elif block.type == "blockp1" or block.type == "blockp2":
                if block.type == "blockp1":
                    for portal in blocks.sprites():
                        if portal.type == "blockp2":
                            moving = None
                            if pacman.moving_down:
                                pacman.x = portal.rect.x - 3
                                pacman.y = portal.rect.y + 33
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                moving = "down"
                            elif pacman.moving_right:
                                pacman.x = portal.rect.x + 33
                                pacman.y = portal.rect.y - 3
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                moving = "right"
                            elif pacman.moving_left:
                                pacman.x = portal.rect.x - 33
                                pacman.y = portal.rect.y - 3
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                moving = "left"
                            elif pacman.moving_up:
                                pacman.x = portal.rect.x - 3
                                pacman.y = portal.rect.y - 33
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                moving = "up"
                            if checkobjectwallcollisions(pacman, blocks, settings):
                                if moving == "down":
                                    pacman.x = portal.rect.x + 3
                                    pacman.y = portal.rect.y - 33
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                elif moving == "right":
                                    pacman.x = portal.rect.x + 33
                                    pacman.y = portal.rect.y + 3
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                elif moving == "left":
                                    pacman.x = portal.rect.x - 33
                                    pacman.y = portal.rect.y + 3
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                elif moving == "up":
                                    pacman.x = portal.rect.x + 3
                                    pacman.y = portal.rect.y + 33
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                pacman.x = portal.rect.x - 3
                                pacman.y = portal.rect.y + 33
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                if checkobjectwallcollisions(pacman, blocks, settings):
                                    pacman.x = portal.rect.x + 3
                                    pacman.y = portal.rect.y - 33
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                    pacman.x = portal.rect.x - 3
                                    pacman.y = portal.rect.y - 33
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                    if checkobjectwallcollisions(pacman, blocks, settings):
                                        pacman.x = portal.rect.x + 3
                                        pacman.y = portal.rect.y + 33
                                        pacman.rect.x = pacman.x
                                        pacman.rect.y = pacman.y
                                        pacman.x = portal.rect.x - 33
                                        pacman.y = portal.rect.y - 3
                                        pacman.rect.x = pacman.x
                                        pacman.rect.y = pacman.y
                                        if checkobjectwallcollisions(pacman, blocks, settings):
                                            pacman.x = portal.rect.x + 33
                                            pacman.y = portal.rect.y + 3
                                            pacman.rect.x = pacman.x
                                            pacman.rect.y = pacman.y
                                            pacman.x = portal.rect.x + 33
                                            pacman.y = portal.rect.y + 3
                                            pacman.rect.x = pacman.x
                                            pacman.rect.y = pacman.y
                            portal.type = "wall"
                            block.type = "wall"
                            settings.portal_passed = True
                elif block.type == "blockp2":
                    for portal in blocks.sprites():
                        if portal.type == "blockp1":
                            moving = None
                            if pacman.moving_down:
                                pacman.x = portal.rect.x - 3
                                pacman.y = portal.rect.y + 33
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                moving = "down"
                            elif pacman.moving_right:
                                pacman.x = portal.rect.x + 33
                                pacman.y = portal.rect.y - 3
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                moving = "right"
                            elif pacman.moving_left:
                                pacman.x = portal.rect.x - 33
                                pacman.y = portal.rect.y - 3
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                moving = "left"
                            elif pacman.moving_up:
                                pacman.x = portal.rect.x - 3
                                pacman.y = portal.rect.y - 33
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                moving = "up"
                            if checkobjectwallcollisions(pacman, blocks, settings):
                                if moving == "down":
                                    pacman.x = portal.rect.x + 3
                                    pacman.y = portal.rect.y - 33
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                elif moving == "right":
                                    pacman.x = portal.rect.x + 33
                                    pacman.y = portal.rect.y + 3
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                elif moving == "left":
                                    pacman.x = portal.rect.x - 33
                                    pacman.y = portal.rect.y + 3
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                elif moving == "up":
                                    pacman.x = portal.rect.x + 3
                                    pacman.y = portal.rect.y + 33
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                pacman.x = portal.rect.x - 3
                                pacman.y = portal.rect.y + 33
                                pacman.rect.x = pacman.x
                                pacman.rect.y = pacman.y
                                if checkobjectwallcollisions(pacman, blocks, settings):
                                    pacman.x = portal.rect.x + 3
                                    pacman.y = portal.rect.y - 33
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                    pacman.x = portal.rect.x - 3
                                    pacman.y = portal.rect.y - 33
                                    pacman.rect.x = pacman.x
                                    pacman.rect.y = pacman.y
                                    if checkobjectwallcollisions(pacman, blocks, settings):
                                        pacman.x = portal.rect.x + 3
                                        pacman.y = portal.rect.y + 33
                                        pacman.rect.x = pacman.x
                                        pacman.rect.y = pacman.y
                                        pacman.x = portal.rect.x - 33
                                        pacman.y = portal.rect.y - 3
                                        pacman.rect.x = pacman.x
                                        pacman.rect.y = pacman.y
                                        if checkobjectwallcollisions(pacman, blocks, settings):
                                            pacman.x = portal.rect.x + 33
                                            pacman.y = portal.rect.y + 3
                                            pacman.rect.x = pacman.x
                                            pacman.rect.y = pacman.y
                                            pacman.x = portal.rect.x + 33
                                            pacman.y = portal.rect.y + 3
                                            pacman.rect.x = pacman.x
                                            pacman.rect.y = pacman.y
                            portal.type = "wall"
                            block.type = "wall"
                            settings.portal_passed = True


def checkdotpacmancollisions(settings, pacman, blocks, ghosts):
    for block in blocks.sprites():
        if pygame.sprite.collide_rect(pacman, block):
            if block.type == "pacdot" and not block.hascollided:
                sound = pygame.mixer.Sound('sounds/pacman_chomp.wav')
                if not pygame.mixer.Channel(2).get_busy():
                    settings.channel3.play(sound, 1)
                block.color = (0, 0, 0)
                settings.score += 10
                settings.dotcount -= 1
                block.hascollided = True
                return block.type
            elif block.type == "ghostkiller" and not block.hascollided:
                block.color = (0, 0, 0)
                block.hascollided = True
                settings.score += 50
                settings.dotcount -= 1
                settings.ghostrunningplayed = False
                for ghost in ghosts.sprites():
                    if ghost.mode == "chasing" or "scatter" in ghost.mode:
                        ghost.run = True
                        ghost.mode = "scatter1"
                        ghost.image = ghost.ghostrun1
                        settings.ghostsrunning = True
            if block.coordcount > 0:
                return block.coordcount


def getnode(obj, blocks):
    for block in blocks.sprites():
        if pygame.sprite.collide_rect(obj, block):
            if block.coordcount >= 0:
                return block.coordcount


def checkobjectwallcollisions(obj, blocks, settings):
    for block in blocks.sprites():
        if pygame.sprite.collide_rect(obj, block):
            if obj.type == "pacman":
                if block.type == "wall" or block.type == "gate" or block.type == "fill" or \
                        (settings.active_portals == 1 and block.type == "blockp1"):
                    return True
            else:
                if block.type == "wall" or block.type == "blockp1" or block.type == "blockp2":
                    if obj.type == "portalbullet":
                        obj.colx = block.rect.x
                        obj.coly = block.rect.y
                    return True
    return False


def checkghostpacmancollisions(settings, screen, ghosts, blocks, pacman):
    for ghost in ghosts.sprites():
        if pygame.sprite.collide_rect(pacman, ghost):
            if not ghost.run:
                pygame.mixer.music.load('sounds/pacman_death.wav')
                pygame.mixer.music.play(1)
                settings.paclives -= 1
                settings.disable_keystrokes = True
                livelost(settings, screen, ghosts, blocks, pacman)
                settings.channel1.stop()
            else:
                if not ghost.runhit:
                    score = settings.ghostseaten * 200
                    pygame.mixer.music.load('sounds/pacman_eatghost.wav')
                    pygame.mixer.music.play(1)
                    textfont = pygame.font.SysFont(None, 20)
                    text = textfont.render(str(score), False, (255, 255, 255))
                    screen.blit(text, (ghost.rect.x, ghost.rect.y))
                    pygame.display.flip()
                    sleep(0.5)
                    ghost.run = True
                    ghost.runhit = True
                    settings.ghostseaten += 1
                    settings.score += score
                    ghost.mode = "retreat"
            break


def checkghostcanmove(ghost, settings, blocks, direction, onlycheck):
    hascollided = True
    if direction == "left":
        ghost.x -= settings.ghostspeed
        ghost.rect.x = ghost.x
        if not checkobjectwallcollisions(ghost, blocks, settings):
            hascollided = False
        if onlycheck or hascollided:
            ghost.x += settings.ghostspeed
            ghost.rect.x = ghost.x
    elif direction == "right":
        ghost.x += settings.ghostspeed
        ghost.rect.x = ghost.x
        if not checkobjectwallcollisions(ghost, blocks, settings):
            hascollided = False
        if onlycheck or hascollided:
            ghost.x -= settings.ghostspeed
            ghost.rect.x = ghost.x
    elif direction == "up":
        ghost.y -= settings.ghostspeed
        ghost.rect.y = ghost.y
        if not checkobjectwallcollisions(ghost, blocks, settings):
            hascollided = False
        if onlycheck or hascollided:
            ghost.y += settings.ghostspeed
            ghost.rect.y = ghost.y
    elif direction == "down":
        ghost.y += settings.ghostspeed
        ghost.rect.y = ghost.y
        if not checkobjectwallcollisions(ghost, blocks, settings):
            hascollided = False
        if onlycheck or hascollided:
            ghost.y -= settings.ghostspeed
            ghost.rect.y = ghost.y
    return not hascollided
