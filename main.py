import pygame
import keystrokes
import checkcollisions
import ghosts_ai
import animate
import miscellaneous as misc

from settings import Settings
from pygame.sprite import Group
from draw_pacman import DrawPacman
from draw_scoreboard import Scoreboard
from buttons import Button
from draw_ghosts import DrawGhosts
from draw_grid import DrawGrid


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Pac-Man Portal")

    blocks = Group()
    ghosts = Group()
    pacman = DrawPacman(settings, screen)
    portal_bullet = Group()
    portals = Group()
    fruits = Group()
    scoreboard = Scoreboard(settings, screen)
    play_button = Button(screen, "Play", 1)
    highscore_button = Button(screen, "High Scores", 2)
    back_button = Button(screen, "Back", 3)

    screen_updates = 0
    pacman_frame = 1
    pacman_rotate = 0
    pacman_deathframe = 1
    ghost_frame = 1
    ghost_runframe = 1

    titleanimation = 1
    titlenewloop = True
    titleghostcount = 1
    titletimer = 0
    titledrawpacman = False
    musicplayed = False
    sound1 = pygame.mixer.Sound('sounds/ghosts_ambient.wav')
    sound1.set_volume(0.1)
    sound2 = pygame.mixer.Sound('sounds/ghosts_ambient_scared1.wav')
    sound2.set_volume(0.2)
    running = True

    while running:
        screen_updates += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            else:
                if not settings.disable_keystrokes:
                    keystrokes.check_events(event, pacman, portal_bullet,  screen, settings, ghosts, blocks, fruits,
                                            play_button, highscore_button, back_button)
        screen.fill(settings.bg_color)
        if settings.titlescreen_active and running:

            screen.blit(pygame.image.load('images/title.png'), (65, 50))
            play_button.draw_button()
            highscore_button.draw_button()
            if settings.resettitleanimation:
                pacman.x = -40
                pacman.y = 340
                pacman.rect.x = pacman.x
                pacman.rect.y = pacman.y
                for ghost in ghosts.sprites():
                    ghosts.remove(ghost)
                for block in blocks.sprites():
                    blocks.remove(block)
                titleanimation = 1
                titlenewloop = True
                titleghostcount = 1
                titletimer = 0
                titledrawpacman = False
                settings.resettitleanimation = False
                musicplayed = False

            if titleanimation == 1:
                if titlenewloop:
                    if not musicplayed:
                        pygame.mixer.music.load('sounds/pacman_intermission.wav')
                        pygame.mixer.music.play(-1)
                        musicplayed = True
                    titletimer += 1
                    if titletimer == 100:
                        pacman.x = -40
                        pacman.y = 340
                        pacman.rect.x = pacman.x
                        pacman.rect.y = pacman.y
                        for i in range(1, 5):
                            ghost = DrawGhosts(settings, screen, i)
                            ghost.x = (i * 40) - 320
                            ghost.y = 340
                            ghost.rect.x = ghost.x
                            ghost.rect.y = ghost.y
                            ghosts.add(ghost)

                        powerpill = DrawGrid(screen)
                        powerpill.color = (255, 255, 255)
                        powerpill.x = 700
                        powerpill.y = 350
                        powerpill.rect.x = powerpill.x
                        powerpill.rect.y = powerpill.y
                        powerpill.block_size = 10
                        powerpill.outline = 0
                        blocks.add(powerpill)
                        titlenewloop = False
                        titletimer = 0
                        titledrawpacman = True

                for ghost in ghosts.sprites():
                    ghost.x += 2
                    ghost.rect.x = ghost.x

                if titledrawpacman:
                    pacman.x += 2
                    pacman.rect.x = pacman.x

                for block in blocks.sprites():
                    if pygame.sprite.collide_rect(pacman, block):
                        blocks.remove(block)
                        titleanimation = 2
                        break
            elif titleanimation == 2:
                for ghost in ghosts.sprites():
                    ghost.x -= 1
                    ghost.rect.x = ghost.x

                pacman.x -= 2
                pacman.rect.x = pacman.x

                for ghost in ghosts.sprites():
                    if pygame.sprite.collide_rect(pacman, ghost):
                        ghosts.remove(ghost)
                if pacman.rect.x <= -33:
                    titleanimation = 3
                    titlenewloop = True
                    titledrawpacman = False
            elif titleanimation == 3:
                if titlenewloop:
                    titletimer += 1
                    if titletimer == 100:
                        ghost = DrawGhosts(settings, screen, titleghostcount)
                        ghost.x = -40
                        ghost.y = 340
                        ghost.rect.x = ghost.x
                        ghost.rect.y = ghost.y
                        ghosts.add(ghost)
                        ghost.type = "blinky"
                        titlenewloop = False
                        titleghostcount += 1
                        titletimer = 0
                for ghost in ghosts.sprites():
                    if ghost.rect.x != 550:
                        ghost.x += 2
                        ghost.rect.x = ghost.x
                        if ghost.rect.x > 805:
                            if ghost.type == "inkey":
                                titleanimation = 1
                                titleghostcount = 1
                                ghosts.remove(ghost)
                                titlenewloop = True
                                break
                            ghosts.remove(ghost)
                    else:
                        titletimer += 1
                        if titletimer == 100:
                            titletimer = 0
                            ghost.x += 2
                            ghost.rect.x = ghost.x
                            if titleghostcount != 5:
                                newghost = DrawGhosts(settings, screen, titleghostcount)
                                newghost.x = -40
                                newghost.y = 340
                                newghost.rect.x = newghost.x
                                newghost.rect.y = newghost.y
                                if titleghostcount == 2:
                                    newghost.type = "pinky"
                                elif titleghostcount == 3:
                                    newghost.type = "clyde"
                                elif titleghostcount == 4:
                                    newghost.type = "inkey"
                                ghosts.add(newghost)

                                newghost.x += 2
                                newghost.rect.x = newghost.x
                                titleghostcount += 1
                        else:
                            textfont = pygame.font.SysFont(None, 50)
                            text = None
                            if ghost.type == "blinky":
                                text = textfont.render("\"blinky\"", False, (246, 4, 4))
                            elif ghost.type == "pinky":
                                text = textfont.render("\"pinky\"", False, (184, 126, 127))
                            elif ghost.type == "clyde":
                                text = textfont.render("\"clyde\"", False, (242, 144, 70))
                            elif ghost.type == "inkey":
                                text = textfont.render("\"inkey\"", False, (109, 247, 251))
                            screen.blit(text, (300, 340))

            if screen_updates % 10 == 0:
                if titleanimation == 1 or titleanimation == 3:
                    if titledrawpacman:
                        if pacman_frame == 1:
                            pacman.image = pacman.pacman_move1
                        elif pacman_frame == 2:
                            pacman.image = pacman.pacman_move2
                        elif pacman_frame == 3:
                            pacman.image = pacman.pacman_move3
                        elif pacman_frame == 4:
                            pacman.image = pacman.pacman_move4
                    for ghost in ghosts.sprites():
                        if ghost.type == "blinky":
                            if ghost_frame == 1:
                                ghost.image = ghost.blinkyright1
                            elif ghost_frame == 2:
                                ghost.image = ghost.blinkyright2
                        elif ghost.type == "clyde":
                            if ghost_frame == 1:
                                ghost.image = ghost.clyderight1
                            elif ghost_frame == 2:
                                ghost.image = ghost.clyderight2
                        elif ghost.type == "pinky":
                            if ghost_frame == 1:
                                ghost.image = ghost.pinkyright1
                            elif ghost_frame == 2:
                                ghost.image = ghost.pinkyright2
                        elif ghost.type == "inkey":
                            if ghost_frame == 1:
                                ghost.image = ghost.inkeyright1
                            elif ghost_frame == 2:
                                ghost.image = ghost.inkeyright2
                elif titleanimation == 2:
                    if pacman_frame == 1:
                        pacman.image = pygame.transform.rotate(pacman.pacman_move1, 180)
                    elif pacman_frame == 2:
                        pacman.image = pygame.transform.rotate(pacman.pacman_move2, 180)
                    elif pacman_frame == 3:
                        pacman.image = pygame.transform.rotate(pacman.pacman_move3, 180)
                    elif pacman_frame == 4:
                        pacman.image = pygame.transform.rotate(pacman.pacman_move4, 180)
                    for ghost in ghosts.sprites():
                        if ghost_frame == 1:
                            ghost.image = ghost.ghostrun1
                        elif ghost_frame == 2:
                            ghost.image = ghost.ghostrun2

            if screen_updates % 10 == 0:
                if pacman_frame == 4:
                    pacman_frame = 1
                else:
                    pacman_frame += 1

                if ghost_frame == 1:
                    ghost_frame = 2
                elif ghost_frame == 2:
                    ghost_frame = 1

            for ghost in ghosts.sprites():
                ghost.draw_ghost()
            if titledrawpacman:
                pacman.blitme()
            for block in blocks.sprites():
                block.draw_block()

        elif settings.highscorescreen_active and running:
            f = open("text/high_scores.txt", "r")
            arr = []
            for line in f:
                arr.append(int(line))
            sort_arr = sorted(arr, reverse=True)

            titlefont = pygame.font.SysFont(None, 75)
            scorefont = pygame.font.SysFont(None, 50)
            titlehighscore = titlefont.render("High Scores", False, (78, 182, 0))
            score1 = scorefont.render("1. ", False, (255, 255, 255))
            score2 = scorefont.render("2. ", False, (255, 255, 255))
            score3 = scorefont.render("3. ", False, (255, 255, 255))
            score4 = scorefont.render("4. ", False, (255, 255, 255))
            score5 = scorefont.render("5. ", False, (255, 255, 255))
            score6 = scorefont.render("6. ", False, (255, 255, 255))
            score7 = scorefont.render("7. ", False, (255, 255, 255))
            score8 = scorefont.render("8. ", False, (255, 255, 255))
            score9 = scorefont.render("9. ", False, (255, 255, 255))
            score10 = scorefont.render("10. ", False, (255, 255, 255))
            screen.blit(titlehighscore, (250, 50))
            screen.blit(score1, (325, 125))
            screen.blit(score2, (325, 175))
            screen.blit(score3, (325, 225))
            screen.blit(score4, (325, 275))
            screen.blit(score5, (325, 325))
            screen.blit(score6, (325, 375))
            screen.blit(score7, (325, 425))
            screen.blit(score8, (325, 475))
            screen.blit(score9, (325, 525))
            screen.blit(score10, (325, 575))

            count = 0
            for num in sort_arr:
                count += 1
                if count <= 10:
                    score = scorefont.render(str(num), False, (255, 255, 255))
                    screen.blit(score, (425, (75 + (50 * count))))
                else:
                    break
            f.close()

            back_button.draw_button()

        elif settings.playing and running:
            if settings.gamestarttimer != 180:
                if not settings.beginningmusicplayed:
                    pygame.mixer.music.load('sounds/pacman_beginning.wav')
                    pygame.mixer.music.play(1)
                    settings.beginningmusicplayed = True
                settings.gamestarttimer += 1
                settings.disable_keystrokes = True
            else:
                for ghost in ghosts.sprites():
                    if ghost.mode == "running" or ghost.run or ghost.runhit or ghost.mode == "retreat":
                        if not settings.ghostrunningplayed:
                            settings.channel1.stop()
                            settings.channel2.play(sound2, -1)
                            settings.ghostrunningplayed = True
                    else:
                        if not settings.ambientghostplayed:
                            settings.channel2.stop()
                            settings.channel1.play(sound1, -1)
                            settings.ambientghostplayed = True

                settings.disable_keystrokes = False
                if settings.dotcount == 0:
                    misc.levelcompleted(settings, screen, ghosts, blocks, pacman, fruits)

                checkcollisions.checkqueuepacwall(settings, pacman, blocks)
                checkcollisions.checkregularpacwall(settings, pacman, blocks)
                checkcollisions.checktunnelpacmancollisions(settings, pacman, blocks)
                checkcollisions.checkghostpacmancollisions(settings, screen, ghosts, blocks, pacman)
                checkcollisions.checkfruitpacmancollisions(settings, pacman, fruits)
                checkcollisions.checkdotpacmancollisions(settings, pacman, blocks, ghosts)
                checkcollisions.checkpacmanportals(settings, screen, blocks, portals, portal_bullet)

                for bullet in portal_bullet.sprites():
                    bullet.update_bullet(pacman)

                misc.checkghostruntimer(settings, ghosts)

                for ghost in ghosts.sprites():
                    ghosts_ai.determine_move(settings, ghost, ghosts, pacman, blocks, screen)

            animate.animate_pacman(pacman, screen_updates, pacman_frame, pacman_rotate, pacman_deathframe, settings,
                                   screen, ghosts, blocks)
            animate.animate_ghosts(settings, ghosts, ghost_frame, ghost_runframe, screen_updates)

            misc.creategridfruit(settings, screen, fruits, blocks)
            for fruit in fruits.sprites():
                fruit.draw_fruit()

            if screen_updates % 10 == 0:
                if pacman_frame == 4:
                    pacman_frame = 1
                else:
                    pacman_frame += 1

                if ghost_frame == 1 or ghost_runframe == 1:
                    ghost_frame = 2
                    ghost_runframe = 2
                elif ghost_frame == 2 or ghost_runframe == 2:
                    ghost_frame = 1
                    ghost_runframe = 1

            if pacman.destruct and screen_updates % 5 == 0:
                if pacman_deathframe == 16:
                    pacman_deathframe = 1
                else:
                    pacman_deathframe += 1

            for block in blocks.sprites():
                block.draw_block()
            for fruit in fruits.sprites():
                fruit.blitme()
            for portal in portals.sprites():
                portal.blitme()
            for bullet in portal_bullet.sprites():
                bullet.draw_bullet()
            for ghost in ghosts.sprites():
                ghost.draw_ghost()
            pacman.blitme()
            scoreboard.update_lives()
            scoreboard.update_scoreboard()
            portaltextfont = pygame.font.SysFont(None, 25)
            portaltext = portaltextfont.render("Press Space to fire a Portal (Max: 2)", False, (255, 255, 255))
            screen.blit(portaltext, (260, 5))

        pygame.display.flip()


run_game()
