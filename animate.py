import pygame

from miscellaneous import livelost


def animate_pacman(pacman, screen_updates, pacman_frame, pacman_rotate, pacman_deathframe, settings, screen, ghosts,
                   blocks):
    if not pacman.destruct:
        if pacman.moving_left:
            pacman_rotate = 180
        elif pacman.moving_down:
            pacman_rotate = -90
        elif pacman.moving_up:
            pacman_rotate = 90
        elif pacman.moving_right:
            pacman_rotate = 0

        if pacman.moving:
            if screen_updates % 10 == 0:
                if pacman_frame == 1:
                    pacman.image = pygame.transform.rotate(pacman.pacman_move1, pacman_rotate)
                elif pacman_frame == 2:
                    pacman.image = pygame.transform.rotate(pacman.pacman_move2, pacman_rotate)
                elif pacman_frame == 3:
                    pacman.image = pygame.transform.rotate(pacman.pacman_move3, pacman_rotate)
                elif pacman_frame == 4:
                    pacman.image = pygame.transform.rotate(pacman.pacman_move4, pacman_rotate)
    else:
        if screen_updates % 5 == 0:
            pacman.death_framecount += 1
            if pacman.death_framecount != 17:
                if pacman_deathframe == 1:
                    pacman.image = pacman.pacman_deathmove1
                elif pacman_deathframe == 2:
                    pacman.image = pacman.pacman_deathmove2
                elif pacman_deathframe == 3:
                    pacman.image = pacman.pacman_deathmove3
                elif pacman_deathframe == 4:
                    pacman.image = pacman.pacman_deathmove4
                elif pacman_deathframe == 5:
                    pacman.image = pacman.pacman_deathmove5
                elif pacman_deathframe == 6:
                    pacman.image = pacman.pacman_deathmove6
                elif pacman_deathframe == 7:
                    pacman.image = pacman.pacman_deathmove7
                elif pacman_deathframe == 8:
                    pacman.image = pacman.pacman_deathmove8
                elif pacman_deathframe == 9:
                    pacman.image = pacman.pacman_deathmove9
                elif pacman_deathframe == 10:
                    pacman.image = pacman.pacman_deathmove10
                elif pacman_deathframe == 11:
                    pacman.image = pacman.pacman_deathmove11
                elif pacman_deathframe == 12:
                    pacman.image = pacman.pacman_deathmove12
                elif pacman_deathframe == 13:
                    pacman.image = pacman.pacman_deathmove13
                elif pacman_deathframe == 14:
                    pacman.image = pacman.pacman_deathmove14
                elif pacman_deathframe == 15:
                    pacman.image = pacman.pacman_deathmove15
                elif pacman_deathframe == 16:
                    pacman.image = pacman.pacman_deathmove16
            else:
                livelost(settings, screen, ghosts, blocks, pacman)


def animate_ghosts(settings, ghosts, ghost_frame, ghost_runframe, screen_updates):
    if screen_updates % 10 == 0:
        for ghost in ghosts.sprites():
            if not ghost.run and not ghost.runhit:
                if ghost.type == "blinky":
                    if ghost.moving_right:
                        if ghost_frame == 1:
                            ghost.image = ghost.blinkyright1
                        elif ghost_frame == 2:
                            ghost.image = ghost.blinkyright2
                    elif ghost.moving_left:
                        if ghost_frame == 1:
                            ghost.image = ghost.blinkyleft1
                        elif ghost_frame == 2:
                            ghost.image = ghost.blinkyleft2
                    elif ghost.moving_up or ghost.mode == "idle":
                        if ghost_frame == 1:
                            ghost.image = ghost.blinkyup1
                        elif ghost_frame == 2:
                            ghost.image = ghost.blinkyup2
                    elif ghost.moving_down:
                        if ghost_frame == 1:
                            ghost.image = ghost.blinkydown1
                        elif ghost_frame == 2:
                            ghost.image = ghost.blinkydown2
                elif ghost.type == "clyde":
                    if ghost.moving_right:
                        if ghost_frame == 1:
                            ghost.image = ghost.clyderight1
                        elif ghost_frame == 2:
                            ghost.image = ghost.clyderight2
                    elif ghost.moving_left:
                        if ghost_frame == 1:
                            ghost.image = ghost.clydeleft1
                        elif ghost_frame == 2:
                            ghost.image = ghost.clydeleft2
                    elif ghost.moving_up or ghost.mode == "idle":
                        if ghost_frame == 1:
                            ghost.image = ghost.clydeup1
                        elif ghost_frame == 2:
                            ghost.image = ghost.clydeup2
                    elif ghost.moving_down:
                        if ghost_frame == 1:
                            ghost.image = ghost.clydedown1
                        elif ghost_frame == 2:
                            ghost.image = ghost.clydedown2
                elif ghost.type == "pinky":
                    if ghost.moving_right:
                        if ghost_frame == 1:
                            ghost.image = ghost.pinkyright1
                        elif ghost_frame == 2:
                            ghost.image = ghost.pinkyright2
                    elif ghost.moving_left:
                        if ghost_frame == 1:
                            ghost.image = ghost.pinkyleft1
                        elif ghost_frame == 2:
                            ghost.image = ghost.pinkyleft2
                    elif ghost.moving_up or ghost.mode == "idle":
                        if ghost_frame == 1:
                            ghost.image = ghost.pinkyup1
                        elif ghost_frame == 2:
                            ghost.image = ghost.pinkyup2
                    elif ghost.moving_down:
                        if ghost_frame == 1:
                            ghost.image = ghost.pinkydown1
                        elif ghost_frame == 2:
                            ghost.image = ghost.pinkydown2
                elif ghost.type == "inkey":
                    if ghost.moving_right:
                        if ghost_frame == 1:
                            ghost.image = ghost.inkeyright1
                        elif ghost_frame == 2:
                            ghost.image = ghost.inkeyright2
                    elif ghost.moving_left:
                        if ghost_frame == 1:
                            ghost.image = ghost.inkeyleft1
                        elif ghost_frame == 2:
                            ghost.image = ghost.inkeyleft2
                    elif ghost.moving_up or ghost.mode == "idle":
                        if ghost_frame == 1:
                            ghost.image = ghost.inkeyup1
                        elif ghost_frame == 2:
                            ghost.image = ghost.inkeyup2
                    elif ghost.moving_down:
                        if ghost_frame == 1:
                            ghost.image = ghost.inkeydown1
                        elif ghost_frame == 2:
                            ghost.image = ghost.inkeydown2

            if ghost.run or ghost.runhit:
                if settings.timer < 200:
                    if ghost_frame == 1:
                        ghost.image = ghost.ghostrun1
                    elif ghost_frame == 2:
                        ghost.image = ghost.ghostrun2
                elif settings.timer >= 200:
                    if ghost_runframe == 1:
                        if ghost_frame == 1:
                            ghost.image = ghost.ghostrun1
                        elif ghost_frame == 2:
                            ghost.image = ghost.ghostrun2
                    elif ghost_runframe == 2:
                        if ghost_frame == 1:
                            ghost.image = ghost.ghost2run1
                        elif ghost_frame == 2:
                            ghost.image = ghost.ghost2run2
