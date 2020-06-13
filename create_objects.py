import pygame

from draw_grid import DrawGrid
from draw_ghosts import DrawGhosts


def create_grid(settings, screen, blocks):
    file = open("text/pacman grid.txt", "r")
    y = 0
    offset = 30
    block_size = 30
    coords = 0
    for line in file:
        y += 1
        x = 0
        for char in line:
            x += 1
            if char != "\n":
                block = DrawGrid(screen)
            else:
                block = None
            if char == 'W':
                block.rect.x = (x * offset) - 60
                block.rect.y = (y * offset) - 29
                block.block_size = 27
                block.outline = 1
                block.type = "wall"
                block.color = (0, 0, 255)
            elif char == 'G':
                block.rect.x = (x * offset) - 60
                block.rect.y = (y * offset) - 29
                block.block_size = 27
                block.outline = 5
                block.color = (255, 255, 255)
                block.type = "gate"
                block.coordcount = 0
            elif char == 'D':
                coords += 1
                if coords == 31 or coords == 43 or coords == 182 or coords == 204:
                    block.color = (255, 255, 255)
                    block.rect.x = (x * offset) - 49
                    block.rect.y = (y * offset) - 21
                    block.block_size = block_size / 3
                    block.hascollided = False
                    block.type = "ghostkiller"
                else:
                    block.color = (255, 255, 0)
                    block.rect.x = (x * offset) - 46
                    block.rect.y = (y * offset) - 16
                    block.block_size = block_size / 7
                    block.hascollided = False
                    block.type = "pacdot"
                block.outline = 0
                settings.dotcount += 1
                block.coordcount = coords
            elif char == 'H':
                block = DrawGrid(screen)
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size / 7
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "pachome"
                block.coordcount = 0
            elif char == 'O':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size / 7
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "open"
                coords += 1
                block.coordcount = coords
            elif char == 'S':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "start"
                coords += 1
                block.coordcount = coords
            elif char == '1':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size / 7
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "tunnel1"
            elif char == '2':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size / 7
                block.outline = 0
                block.color = (255, 0, 0)
                block.type = "tunnel2"
            elif char == 'B':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size / 7
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "blinky"
                block.coordcount = 0
            elif char == 'P':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "pinky"
                block.coordcount = 0
            elif char == 'I':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "inkey"
                block.coordcount = 0
            elif char == 'C':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "clyde"
                block.coordcount = 0
            elif char == 'X':
                block.rect.x = (x * offset) - 46
                block.rect.y = (y * offset) - 16
                block.block_size = block_size / 7
                block.outline = 0
                block.color = (0, 0, 0)
                block.type = "fill"
            if char != "\n":
                block.rect = pygame.Rect(block.rect.x, block.rect.y, block.block_size, block.block_size)
                blocks.add(block)


def create_ghosts(settings, screen, ghosts, blocks, num):
    for block in blocks.sprites():
        if block.type == 'blinky' and (num == "blinky" or num == "all"):
            ghost = DrawGhosts(settings, screen, 1)
            ghost.x = block.rect.x - 17
            ghost.y = block.rect.y - 16
            ghost.rect.x = ghost.x
            ghost.rect.y = ghost.y
            ghost.mode = "exiting"
            ghosts.add(ghost)
        elif block.type == 'pinky' and (num == "pinky" or num == "all"):
            ghost = DrawGhosts(settings, screen, 2)
            ghost.x = block.rect.x - 17
            ghost.y = block.rect.y - 16
            ghost.rect.x = ghost.x
            ghost.rect.y = ghost.y
            ghost.mode = "idle"
            ghosts.add(ghost)
        elif block.type == 'clyde' and (num == "clyde" or num == "all"):
            ghost = DrawGhosts(settings, screen, 3)
            ghost.x = block.rect.x - 17
            ghost.y = block.rect.y - 16
            ghost.rect.x = ghost.x
            ghost.rect.y = ghost.y
            ghost.mode = "idle"
            ghosts.add(ghost)
        elif block.type == 'inkey' and (num == "inkey" or num == "all"):
            ghost = DrawGhosts(settings, screen, 4)
            ghost.x = block.rect.x - 17
            ghost.y = block.rect.y - 16
            ghost.rect.x = ghost.x
            ghost.rect.y = ghost.y
            ghost.mode = "idle"
            ghosts.add(ghost)
