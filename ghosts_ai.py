from create_objects import create_ghosts
import checkcollisions as cc
import random


def scatter_mode(settings, ghost, blocks):
    target = None
    if ghost.type == "blinky":
        if ghost.mode == "scatter1":
            target = 22
        elif ghost.mode == "scatter2":
            target = 43
        elif ghost.mode == "scatter3":
            target = 71
        elif ghost.mode == "scatter4":
            target = 42
    elif ghost.type == "clyde":
        if ghost.mode == "scatter1":
            target = 233
        elif ghost.mode == "scatter2":
            target = 243
        elif ghost.mode == "scatter3":
            target = 219
        elif ghost.mode == "scatter4":
            target = 215
    elif ghost.type == "pinky":
        if ghost.mode == "scatter1":
            target = 3
        elif ghost.mode == "scatter2":
            target = 31
        elif ghost.mode == "scatter3":
            target = 52
        elif ghost.mode == "scatter4":
            target = 32
    elif ghost.type == "inkey":
        if ghost.mode == "scatter1":
            target = 236
        elif ghost.mode == "scatter2":
            target = 253
        elif ghost.mode == "scatter3":
            target = 224
        elif ghost.mode == "scatter4":
            target = 227

    if not move_ghost(settings, ghost, target, blocks, True, False):
        if ghost.mode == "scatter1":
            ghost.mode = "scatter2"
        elif ghost.mode == "scatter2":
            ghost.mode = "scatter3"
        elif ghost.mode == "scatter3":
            ghost.mode = "scatter4"
        elif ghost.mode == "scatter4":
            ghost.mode = "scatter1"


def determine_move(settings, ghost, ghosts, pacman, blocks, screen):
    randint = random.randint(1, 500)
    if randint == 1 and not ghost.run:
        if ghost.mode == "idle":
            ghost.mode = "exiting"
        elif ghost.mode == "chasing" and ghost.type != "clyde":
            ghost.mode = "scatter1"
        elif "scatter" in ghost.mode and ghost.type != "clyde":
            ghost.mode = "chasing"

    if ghost.mode == "exiting":
        if cc.getnode(ghost, blocks) == 0:
            if not cc.checkghostcanmove(ghost, settings, blocks, "up", False):
                if ghost.type == "clyde":
                    ghost.moving_right = False
                    ghost.moving_left = True
                    ghost.moving_up = False
                    ghost.moving_down = False
                    ghost.x -= settings.ghostspeed
                    ghost.rect.x = ghost.x
                elif ghost.type == "inkey":
                    ghost.moving_right = True
                    ghost.moving_left = False
                    ghost.moving_up = False
                    ghost.moving_down = False
                    ghost.x += settings.ghostspeed
                    ghost.rect.x = ghost.x
            else:
                ghost.moving_right = False
                ghost.moving_left = False
                ghost.moving_up = True
                ghost.moving_down = False
        elif cc.getnode(ghost, blocks) > 0:
            if not cc.checkghostcanmove(ghost, settings, blocks, "up", False):
                ghost.mode = "chasing"
    elif ghost.mode == "chasing" and ghost.type != "clyde":
        if ghost.type == "blinky":
            move_ghost(settings, ghost, pacman, blocks, True, True)
        elif ghost.type == "pinky":
            target = cc.getnode(pacman, blocks)
            if target + 4 <= 261 and target - 4 >= 1:
                if pacman.moving_right:
                    move_ghost(settings, ghost, target + 4, blocks, True, False)
                elif pacman.moving_left:
                    move_ghost(settings, ghost, target - 4, blocks, True, False)
                else:
                    move_ghost(settings, ghost, target, blocks, True, False)
            else:
                move_ghost(settings, ghost, target, blocks, True, False)
        elif ghost.type == "inkey":
            blinky = None
            for blinky in ghosts.sprites():
                if ghost.type == "blinky":
                    blinky = ghost.type
                    break
            target = cc.getnode(pacman, blocks)
            if blinky:
                if abs(ghost.rect.x - blinky.rect.x) < abs(ghost.rect.y - blinky.rect.y):
                    if target + abs(ghost.rect.x - blinky.rect.x) <= 261 and target - abs(
                            ghost.rect.x - blinky.rect.x) >= 1:
                        if pacman.moving_right:
                            target = target + abs(ghost.rect.x - blinky.rect.x)
                            move_ghost(settings, ghost, target - 4, blocks, True, False)
                        elif pacman.moving_left:
                            target = target - abs(ghost.rect.x - blinky.rect.x)
                            move_ghost(settings, ghost, target - 4, blocks, True, False)
                        else:
                            move_ghost(settings, ghost, target, blocks, True, False)
                    else:
                        move_ghost(settings, ghost, target, blocks, True, False)
                elif abs(ghost.rect.y - blinky.rect.y) > abs(ghost.rect.x - blinky.rect.x):
                    if target + abs(ghost.rect.x - blinky.rect.x) <= 261 and target - abs(
                            ghost.rect.x - blinky.rect.x) >= 1:
                        if pacman.moving_right:
                            target = target + abs(ghost.rect.x - blinky.rect.x)
                            move_ghost(settings, ghost, target - 4, blocks, True, False)
                        elif pacman.moving_left:
                            target = target - abs(ghost.rect.x - blinky.rect.x)
                            move_ghost(settings, ghost, target - 4, blocks, True, False)
                        else:
                            move_ghost(settings, ghost, target, blocks, True, False)
                    else:
                        move_ghost(settings, ghost, target, blocks, True, False)
                else:
                    move_ghost(settings, ghost, target, blocks, True, False)
            else:
                move_ghost(settings, ghost, target, blocks, True, False)
    elif ghost.type == "clyde" and (ghost.mode == "chasing" or "scatter" in ghost.mode):
        if abs(ghost.rect.x - pacman.rect.x) <= 240 and abs(ghost.rect.y - pacman.rect.y) <= 240:
            move_ghost(settings, ghost, pacman, blocks, True, True)
            cc.checkghostcanmove(ghost, settings, blocks, "up", False)
            ghost.mode = "chasing"
        else:
            if "scatter" not in ghost.mode:
                ghost.mode = "scatter1"
            scatter_mode(settings, ghost, blocks)
    elif ghost.mode == "retreat":
        ghosts.remove(ghost)
        create_ghosts(settings, screen, ghosts, blocks, ghost.type)
        if ghost.type == "blinky":
            ghost.mode = "idle"
    elif ghost.run or "scatter" in ghost.mode:
        scatter_mode(settings, ghost, blocks)


def move_ghost(settings, ghost, target, blocks, findcurrentnode, findtargetnode):
    graph = \
        {1: {25: 1, 2: 1},
         2: {1: 1, 3: 1},
         3: {2: 1, 4: 1},
         4: {3: 1, 5: 1},
         5: {4: 1, 6: 1, 26: 1},
         6: {5: 1, 7: 1},
         7: {6: 1, 8: 1},
         8: {7: 1, 9: 1},
         9: {8: 1, 10: 1},
         10: {9: 1, 11: 1},
         11: {10: 1, 12: 1},
         12: {11: 1, 27: 1},
         13: {28: 1, 14: 1},
         14: {13: 1, 15: 1},
         15: {14: 1, 16: 1},
         16: {15: 1, 17: 1},
         17: {16: 1, 18: 1},
         18: {17: 1, 19: 1},
         19: {18: 1, 20: 1},
         20: {19: 1, 21: 1, 29: 1},
         21: {20: 1, 22: 1},
         22: {21: 1, 23: 1},
         23: {22: 1, 24: 1},
         24: {23: 1, 30: 1},
         25: {1: 1, 31: 1},
         26: {5: 1, 32: 1},
         27: {12: 1, 36: 1},
         28: {13: 1, 38: 1},
         29: {20: 1, 41: 1},
         30: {24: 1, 43: 1},
         31: {25: 1, 44: 1},
         32: {26: 1, 45: 1},
         33: {46: 1, 34: 1},
         34: {33: 1, 35: 1},
         35: {34: 1, 36: 1},
         36: {35: 1, 37: 1, 27: 1},
         37: {36: 1, 38: 1},
         38: {37: 1, 39: 1, 28: 1},
         39: {38: 1, 40: 1},
         40: {39: 1, 41: 1},
         41: {40: 1, 47: 1},
         42: {29: 1, 48: 1},
         43: {30: 1, 49: 1},
         44: {31: 1, 50: 1},
         45: {32: 1, 54: 1},
         46: {33: 1, 58: 1},
         47: {41: 1, 65: 1},
         48: {42: 1, 69: 1},
         49: {43: 1, 73: 1},
         50: {44: 1, 74: 1, 51: 1},
         51: {50: 1, 52: 1},
         52: {51: 1, 53: 1},
         53: {52: 1, 54: 1},
         54: {53: 1, 55: 1, 45: 1, 75: 1},
         55: {54: 1, 56: 1},
         56: {55: 1, 57: 1},
         57: {56: 1, 58: 1},
         58: {57: 1, 59: 1, 46: 1},
         59: {58: 1, 60: 1},
         60: {59: 1, 61: 1},
         61: {60: 1, 76: 1},
         62: {77: 1, 63: 1},
         63: {62: 1, 64: 1},
         64: {63: 1, 65: 1},
         65: {64: 1, 66: 1, 47: 1},
         66: {65: 1, 67: 1},
         67: {66: 1, 68: 1},
         68: {67: 1, 69: 1},
         69: {68: 1, 70: 1, 48: 1, 78: 1},
         70: {69: 1, 71: 1},
         71: {70: 1, 72: 1},
         72: {71: 1, 73: 1},
         73: {49: 1, 79: 1, 72: 1},
         74: {50: 1, 80: 1},
         75: {54: 1, 81: 1},
         76: {61: 1, 85: 1},
         77: {62: 1, 87: 1},
         78: {69: 1, 91: 1},
         79: {73: 1, 92: 1},
         80: {74: 1, 93: 1},
         81: {75: 1, 97: 1},
         82: {100: 1, 83: 1},
         83: {82: 1, 84: 1},
         84: {83: 1, 85: 1},
         85: {84: 1, 86: 1, 76: 1},
         86: {85: 1, 87: 1},
         87: {86: 1, 88: 1, 77: 1},
         88: {87: 1, 89: 1},
         89: {88: 1, 90: 1},
         90: {89: 1, 101: 1},
         91: {78: 1, 104: 1},
         92: {79: 1, 108: 1},
         93: {80: 1, 94: 1},
         94: {93: 1, 95: 1},
         95: {94: 1, 96: 1},
         96: {95: 1, 97: 1},
         97: {96: 1, 98: 1, 81: 1},
         98: {97: 1, 99: 1},
         99: {98: 1, 109: 1},
         100: {82: 1, 110: 1},
         101: {90: 1, 111: 1},
         102: {112: 1, 103: 1},
         103: {102: 1, 104: 1},
         104: {103: 1, 105: 1, 91: 1},
         105: {104: 1, 106: 1},
         106: {105: 1, 107: 1},
         107: {106: 1, 108: 1},
         108: {107: 1, 92: 1},
         109: {99: 1, 113: 1},
         110: {100: 1, 114: 1},
         111: {101: 1, 115: 1},
         112: {102: 1, 116: 1},
         113: {109: 1, 124: 1},
         114: {110: 1, 126: 1},
         115: {111: 1, 127: 1},
         116: {112: 1, 129: 1},
         117: {118: 1},
         118: {117: 1, 119: 1},
         119: {118: 1, 120: 1},
         120: {119: 1, 121: 1},
         121: {120: 1, 122: 1},
         122: {121: 1, 123: 1},
         123: {122: 1, 124: 1},
         124: {113: 1, 137: 1, 123: 1, 125: 1},
         125: {124: 1, 126: 1},
         126: {114: 1, 138: 1, 125: 1},
         127: {115: 1, 146: 1, 128: 1},
         128: {127: 1, 129: 1},
         129: {116: 1, 147: 1, 128: 1, 130: 1},
         130: {129: 1, 131: 1},
         131: {130: 1, 132: 1},
         132: {131: 1, 133: 1},
         133: {132: 1, 134: 1},
         134: {133: 1, 135: 1},
         135: {134: 1, 136: 1},
         136: {135: 1},
         137: {124: 1, 148: 1},
         138: {126: 1, 149: 1, 139: 1},
         139: {138: 1, 140: 1},
         140: {139: 1, 141: 1},
         141: {140: 1, 142: 1},
         142: {141: 1, 143: 1},
         143: {142: 1, 144: 1},
         144: {143: 1, 145: 1},
         145: {144: 1, 146: 1},
         146: {145: 1, 127: 1, 150: 1},
         147: {129: 1, 151: 1},
         148: {137: 1, 158: 1},
         149: {138: 1, 160: 1},
         150: {146: 1, 167: 1},
         151: {147: 1, 169: 1},
         152: {176: 1, 153: 1},
         153: {152: 1, 154: 1},
         154: {153: 1, 155: 1},
         155: {154: 1, 156: 1},
         156: {155: 1, 157: 1, 177: 1},
         157: {156: 1, 158: 1},
         158: {157: 1, 159: 1, 148: 1},
         159: {158: 1, 160: 1},
         160: {159: 1, 161: 1, 149: 1},
         161: {160: 1, 162: 1},
         162: {161: 1, 163: 1},
         163: {162: 1, 178: 1},
         164: {179: 1, 165: 1},
         165: {164: 1, 166: 1},
         166: {165: 1, 167: 1},
         167: {166: 1, 168: 1, 150: 1},
         168: {167: 1, 169: 1},
         169: {168: 1, 170: 1, 151: 1},
         170: {169: 1, 171: 1},
         171: {170: 1, 172: 1, 180: 1},
         172: {171: 1, 173: 1},
         173: {172: 1, 174: 1},
         174: {173: 1, 175: 1},
         175: {174: 1, 181: 1},
         176: {152: 1, 182: 1},
         177: {156: 1, 185: 1},
         178: {163: 1, 192: 1},
         179: {164: 1, 194: 1},
         180: {171: 1, 201: 1},
         181: {175: 1, 204: 1},
         182: {176: 1, 183: 1},
         183: {182: 1, 184: 1},
         184: {183: 1, 205: 1},
         185: {177: 1, 186: 1},
         186: {185: 1, 187: 1},
         187: {186: 1, 188: 1, 206: 1},
         188: {187: 1, 189: 1},
         189: {188: 1, 190: 1, 207: 1},
         190: {189: 1, 191: 1},
         191: {190: 1, 192: 1},
         192: {191: 1, 193: 1, 178: 1},
         193: {192: 1, 194: 1},
         194: {193: 1, 195: 1, 179: 1},
         195: {194: 1, 196: 1},
         196: {195: 1, 197: 1},
         197: {196: 1, 198: 1, 208: 1},
         198: {197: 1, 199: 1},
         199: {198: 1, 200: 1, 209: 1},
         200: {199: 1, 201: 1},
         201: {201: 1, 180: 1},
         202: {210: 1, 203: 1},
         203: {202: 1, 204: 1},
         204: {203: 1, 181: 1},
         205: {184: 1, 213: 1},
         206: {187: 1, 217: 1},
         207: {189: 1, 218: 1},
         208: {197: 1, 225: 1},
         209: {199: 1, 226: 1},
         210: {202: 1, 230: 1},
         211: {233: 1, 212: 1},
         212: {211: 1, 213: 1},
         213: {212: 1, 214: 1, 215: 1},
         214: {213: 1, 215: 1},
         215: {214: 1, 216: 1},
         216: {215: 1, 217: 1},
         217: {216: 1, 206: 1},
         218: {207: 1, 219: 1},
         219: {218: 1, 220: 1},
         220: {219: 1, 221: 1},
         221: {220: 1, 234: 1},
         222: {235: 1, 223: 1},
         223: {222: 1, 224: 1},
         224: {223: 1, 225: 1},
         225: {224: 1, 208: 1},
         226: {209: 1, 227: 1},
         227: {226: 1, 228: 1},
         228: {227: 1, 229: 1},
         229: {228: 1, 230: 1},
         230: {229: 1, 231: 1, 210: 1},
         231: {230: 1, 232: 1},
         232: {231: 1, 236: 1},
         233: {211: 1, 237: 1},
         234: {221: 1, 248: 1},
         235: {222: 1, 250: 1},
         236: {232: 1, 261: 1},
         237: {233: 1, 238: 1},
         238: {237: 1, 239: 1},
         239: {238: 1, 240: 1},
         240: {239: 1, 241: 1},
         241: {240: 1, 242: 1},
         242: {241: 1, 243: 1},
         243: {242: 1, 244: 1},
         244: {243: 1, 245: 1},
         245: {244: 1, 246: 1},
         246: {245: 1, 247: 1},
         247: {246: 1, 248: 1},
         248: {247: 1, 249: 1, 234: 1},
         249: {248: 1, 250: 1},
         250: {249: 1, 251: 1, 235: 1},
         251: {250: 1, 252: 1},
         252: {251: 1, 253: 1},
         253: {252: 1, 254: 1},
         254: {253: 1, 255: 1},
         255: {254: 1, 256: 1},
         256: {255: 1, 257: 1},
         257: {256: 1, 258: 1},
         258: {257: 1, 259: 1},
         259: {258: 1, 260: 1},
         260: {259: 1, 261: 1},
         261: {260: 1, 236: 1}}
    if findcurrentnode:
        currentnode = cc.getnode(ghost, blocks)
    else:
        currentnode = ghost
    if findtargetnode:
        destinationnode = cc.getnode(target, blocks)
    else:
        destinationnode = target

    nextnode = dijkstra(graph, currentnode, destinationnode)

    if nextnode == 0 or nextnode == 'NoneType':
        return False

    if abs(currentnode - nextnode) == 1:
        if currentnode < nextnode:
            ghost.shouldmove_right = True
        else:
            ghost.shouldmove_left = True
    else:
        if currentnode < nextnode:
            ghost.shouldmove_down = True
        else:
            ghost.shouldmove_up = True

    if ghost.shouldmove_right:
        if cc.checkghostcanmove(ghost, settings, blocks, "right", False):
            ghost.moving_right = True
            ghost.moving_left = False
            ghost.moving_up = False
            ghost.moving_down = False
        else:
            ghost.force_ghost = True
    elif ghost.shouldmove_left:
        if cc.checkghostcanmove(ghost, settings, blocks, "left", False):
            ghost.moving_left = True
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = False
        else:
            ghost.force_ghost = True
    elif ghost.shouldmove_down:
        if cc.checkghostcanmove(ghost, settings, blocks, "down", False):
            ghost.moving_down = True
            ghost.moving_up = False
            ghost.moving_right = False
            ghost.moving_left = False
        else:
            ghost.force_ghost = True
    elif ghost.shouldmove_up:
        if cc.checkghostcanmove(ghost, settings, blocks, "up", False):
            ghost.moving_up = True
            ghost.moving_down = False
            ghost.moving_right = False
            ghost.moving_left = False
        else:
            ghost.force_ghost = True

    if ghost.force_ghost:
        if ghost.moving_right:
            ghost.x += settings.ghostspeed
            ghost.rect.x = ghost.x
        elif ghost.moving_left:
            ghost.x -= settings.ghostspeed
            ghost.rect.x = ghost.x
        elif ghost.moving_down:
            ghost.y += settings.ghostspeed
            ghost.rect.y = ghost.y
        elif ghost.moving_up:
            ghost.y -= settings.ghostspeed
            ghost.rect.y = ghost.y

    ghost.force_ghost = False
    ghost.shouldmove_right = False
    ghost.shouldmove_left = False
    ghost.shouldmove_up = False
    ghost.shouldmove_down = False
    return True


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseennodes = graph
    infinity = 9999999
    path = []
    for node in unseennodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseennodes:
        minnode = None
        for node in unseennodes:
            if minnode is None:
                minnode = node
            elif shortest_distance[node] < shortest_distance[minnode]:
                minnode = node

        for childNode, weight in graph[minnode].items():
            if weight + shortest_distance[minnode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minnode]
                predecessor[childNode] = minnode
        unseennodes.pop(minnode)

    currentnode = goal
    while currentnode != start:
        try:
            path.insert(0, currentnode)
            currentnode = predecessor[currentnode]
        except KeyError:
            print('Path not reachable')
            break

    if shortest_distance[goal] != infinity:
        if len(path) > 0:
            return path[0]
        else:
            return 0
