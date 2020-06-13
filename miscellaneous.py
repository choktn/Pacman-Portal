import random
import create_objects

from time import sleep
from fruits import Fruit


def livelost(settings, screen, ghosts, blocks, pacman):
    settings.ghostseaten = 1
    settings.channel1.stop()
    settings.channel2.stop()
    for ghost in ghosts.sprites():
        ghosts.remove(ghost)
    pacman.moving = False
    pacman.moving_right = False
    pacman.moving_left = False
    pacman.moving_up = False
    pacman.moving_down = False
    if pacman.death_framecount != 17:
        pacman.destruct = True
    else:
        pacman.death_framecount = 0
        settings.disable_keystrokes = False
        pacman.destruct = False
        sleep(1)
        if settings.paclives == 0:
            f = open("text/high_scores.txt", "a")
            f.write(str(settings.score) + "\n")
            f.close()
            pacman.image = pacman.pacman_move1
            for block in blocks.sprites():
                blocks.remove(block)
            settings.playing = False
            settings.titlescreen_active = True
            settings.current_level = 1
            settings.paclives = 3
            settings.score = 0
            settings.fruit_created = False
            settings.resettitleanimation = True
            settings.gamestarttimer = 0
            settings.beginningmusicplayed = False
            settings.ambientghostplayed = False
        else:
            pacman.image = pacman.pacman_move1
            pacman.draw_pacman(blocks)
            create_objects.create_ghosts(settings, screen, ghosts, blocks, "all")
            settings.ambientghostplayed = False
            settings.ghostrunningplayed = False


def levelcompleted(settings, screen, ghosts, blocks, pacman, fruits):
    sleep(1)
    settings.current_level += 1
    for ghost in ghosts.sprites():
        ghosts.remove(ghost)
    for block in blocks.sprites():
        blocks.remove(block)
    for fruit in fruits.sprites():
        fruits.remove(fruit)
    if settings.current_level < 8:
        scoreboardfruit = Fruit(screen, settings.current_level)
    else:
        scoreboardfruit = Fruit(screen, 8)
    fruits.add(scoreboardfruit)
    scoreboardfruit.x = 650
    scoreboardfruit.y = 700
    pacman.moving = False
    create_objects.create_grid(settings, screen, blocks)
    pacman.draw_pacman(blocks)
    create_objects.create_ghosts(settings, screen, ghosts, blocks, "all")
    settings.fruit_created = False


def checkghostruntimer(settings, ghosts):
    if settings.ghostsrunning:
        settings.timer += 1
        if settings.timer == 300:
            settings.ghostseaten = 1
            settings.ghostsrunning = False
            settings.ambientghostplayed = False
            for ghost in ghosts.sprites():
                if ghost.run and ghost.mode != "retreat":
                    ghost.run = False
                    ghost.runhit = False
                    if ghost.type == "blinky":
                        ghost.image = ghost.blinky
                    elif ghost.type == "clyde":
                        ghost.image = ghost.clyde
                    elif ghost.type == "pinky":
                        ghost.image = ghost.pinky
                    elif ghost.type == "inkey":
                        ghost.image = ghost.inkey
            settings.timer = 0


def creategridfruit(settings, screen, fruits, blocks):
    if not settings.fruit_created:
        randint = random.randint(1, 3000)
        if randint == 1 or settings.dotcount == 50:
            if settings.current_level < 8:
                gridfruit = Fruit(screen, settings.current_level)
            else:
                gridfruit = Fruit(screen, 8)
            fruits.add(gridfruit)
            for block in blocks.sprites():
                if block.coordcount == 142:
                    gridfruit.x = block.rect.x - 17
                    gridfruit.y = block.rect.y - 16
                    break
            settings.fruit_created = True
            settings.dotcount += 1
