import pygame
import math
import random

pygame.init()

# to do
# get cooler flood fill (doesnt stop at screen edges)
# get death animation (maybe)

# constants
WIDTH = 600
HEIGHT = 600
GRIDSIZE = 20
DENSITY = 8  # higher means lower density # do not set it too low or the code will
FRAMERATE = 20

HIDDENCOLOR = (137, 207, 240)
SHOWNCOLOR = (255, 127, 80)
NUMBACKGROUNDCOLOR = (204, 91, 68)
FLAGCOLOR = (255, 0, 0)

map = []  # 2d list- -9 is hidden no mine negatives are hidden, 0 is nothing, postive are showen, and 9 is a mine


def deathIsCool(screen, map, pos):
    createNewMap(map)
    pos = [2*GRIDSIZE, 2*GRIDSIZE]


def floodFill(map, x, y):  # sigh, flood fill for discovering an area
    if x > 2 and getTrueValue(map[y][x-1]) < 0:
        if map[y][x-1] == -9:
            map[y][x-1] = 0
            floodFill(map, x-1, y)
        else:
            map[y][x-1] = abs(map[y][x-1])
    if x < len(map[0])-3 and getTrueValue(map[y][x+1]) < 0:
        if map[y][x+1] == -9:
            map[y][x+1] = 0
            floodFill(map, x+1, y)
        else:
            map[y][x+1] = abs(map[y][x+1])
    if y > 2 and getTrueValue(map[y-1][x]) < 0:
        if map[y-1][x] == -9:
            map[y-1][x] = 0
            floodFill(map, x, y-1)
        else:
            map[y-1][x] = abs(map[y-1][x])
    if y < len(map)-3 and getTrueValue(map[y+1][x]) < 0:
        if map[y+1][x] == -9:
            map[y+1][x] = 0
            floodFill(map, x, y+1)
        else:
            map[y+1][x] = abs(map[y+1][x])


def getNeighbors(x, y, map):
    total = 0
    if y > 0:
        if getTrueValue(map[y-1][x]) == 9:
            total += 1
        if x > 0 and getTrueValue(map[y-1][x-1]) == 9:
            total += 1
        if x < len(map[0])-1 and getTrueValue(map[y-1][x+1]) == 9:
            total += 1
    if y < len(map) - 1:
        if getTrueValue(map[y+1][x]) == 9:
            total += 1
        if x > 0 and getTrueValue(map[y+1][x-1]) == 9:
            total += 1
        if x < len(map[0])-1 and getTrueValue(map[y+1][x+1]) == 9:
            total += 1
    if x > 0 and getTrueValue(map[y][x-1]) == 9:
        total += 1
    if x < len(map[y])-1 and getTrueValue(map[y][x+1] == 9):
        total += 1
    return total


def getTrueValue(val):
    if type(val) == str:
        return int(val[1:])
    else:
        return val


def asignNumbers(map, index, row):
    if row:
        for ind, i in enumerate(map[index]):
            if i != 9:
                n = getNeighbors(ind, index, map)
                if n != 0:
                    map[index][ind] = -n
    else:
        for ind in range(len(map)):
            if map[ind][index] != 9:
                n = getNeighbors(index, ind, map)
                if n != 0:
                    map[ind][index] = -n


def createRow(map, top):
    row = []
    for i in range(len(map[0])):
        if random.randint(0, DENSITY) == 1:
            row.append(9)
        else:
            row.append(-9)
    if top:
        map.insert(0, row)
        asignNumbers(map, 1, True)
    else:
        map.append(row)
        asignNumbers(map, -2, True)


def createCol(map, top):
    if top:
        for i in range(len(map)):
            if random.randint(0, DENSITY) == 1:
                map[i].insert(0, 9)
            else:
                map[i].insert(0, -9)
        asignNumbers(map, 1, False)
    else:
        for i in range(len(map)):
            if random.randint(0, DENSITY) == 1:
                map[i].append(9)
            else:
                map[i].append(-9)
        asignNumbers(map, -2, False)


def createNewMap(map):
    for y in range(HEIGHT//GRIDSIZE + 4):
        row = []
        for x in range(WIDTH//GRIDSIZE + 4):  # plus 4 bc of a border of 2
            if random.randint(0, DENSITY) == 1:
                row.append(9)
            else:
                row.append(-9)
        map.append(row)


# create the inital map
createNewMap(map)

# asign all the values for the dumb stuff ig
for y in range(2, HEIGHT//GRIDSIZE + 2):
    asignNumbers(map, y, True)
currentPos = [2*GRIDSIZE, 2*GRIDSIZE]


leftMouseButton = False
rightMouseButton = False
mousePressedPosition = (0, 0)
placing = False  # determs if we are trying to place/click

clock = pygame.time.Clock()
mpos = pygame.mouse.get_pos()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('MINESWEEP')

font = pygame.font.Font('freesansbold.ttf', GRIDSIZE)

running = True
print("starting")

while running:
    clock.tick(FRAMERATE)
    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not leftMouseButton and not rightMouseButton:
            if event.button == 1:
                leftMouseButton = True
                mousePressedPosition = mpos
                placing = True
            elif event.button == 3:
                rightMouseButton = True
                mousePressedPosition = mpos
                placing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                leftMouseButton = False
                mousePressedPosition = mpos
                if placing:
                    placingX = (mpos[0] + currentPos[0])//GRIDSIZE
                    placingY = (mpos[1] + currentPos[1])//GRIDSIZE
                    if map[placingY][placingX] == 9:
                        print("YOUR BAD")
                        running = False
                    else:
                        if map[placingY][placingX] == -9:
                            map[placingY][placingX] = 0
                        else:
                            map[placingY][placingX] = abs(
                                getTrueValue(map[placingY][placingX]))
                        floodFill(map, placingX, placingY)
            elif event.button == 3:
                rightMouseButton = False
                mousePressedPosition = mpos
                if placing:
                    placingX = (mpos[0] + currentPos[0])//GRIDSIZE
                    placingY = (mpos[1] + currentPos[1])//GRIDSIZE
                    if type(map[placingY][placingX]) == str:
                        map[placingY][placingX] = int(
                            map[placingY][placingX][1:])
                    else:
                        map[placingY][placingX] = "f" + \
                            str(map[placingY][placingX])

        screen.fill((255, 255, 255))

        # logic stuff ig
        if leftMouseButton and mpos != mousePressedPosition:
            placing = False

            currentPos[0] += mousePressedPosition[0] - mpos[0]
            currentPos[1] += mousePressedPosition[1] - mpos[1]

            mousePressedPosition = mpos

            if currentPos[0] - 2*GRIDSIZE < 0:
                for i in range(math.ceil(abs(currentPos[0]-40)/GRIDSIZE)):
                    createCol(map, True)
                currentPos[0] = 2*GRIDSIZE + currentPos[0] % GRIDSIZE
            if currentPos[1] - 2*GRIDSIZE < 0:
                for i in range(math.ceil(abs(currentPos[1]-40)/GRIDSIZE)):
                    createRow(map, True)
                currentPos[1] = 2*GRIDSIZE + currentPos[1] % GRIDSIZE
            if currentPos[0] + 2*GRIDSIZE + WIDTH > len(map[0])*GRIDSIZE:
                for i in range(math.ceil((currentPos[0] + WIDTH + 40)/GRIDSIZE)-len(map[0])):
                    createCol(map, False)
            if currentPos[1] + 2*GRIDSIZE + HEIGHT > len(map)*GRIDSIZE:
                for i in range(math.ceil((currentPos[1] + HEIGHT + 40)/GRIDSIZE)-len(map)):
                    createRow(map, False)

        # render the stuff
        xThing = currentPos[0] % GRIDSIZE
        yThing = currentPos[1] % GRIDSIZE

        yOffset = currentPos[1]//GRIDSIZE
        xOffset = currentPos[0]//GRIDSIZE
        for y, yVal in enumerate(map[yOffset:yOffset + HEIGHT//GRIDSIZE + GRIDSIZE]):
            for x, xVal in enumerate(yVal[xOffset:xOffset + WIDTH//GRIDSIZE + GRIDSIZE]):
                trueX = getTrueValue(xVal)
                if trueX < 0 or trueX == 9:
                    pygame.draw.rect(
                        screen, HIDDENCOLOR, (x*GRIDSIZE - xThing, y*GRIDSIZE - yThing, GRIDSIZE, GRIDSIZE))
                elif trueX == 0:
                    pygame.draw.rect(
                        screen, SHOWNCOLOR, (x*GRIDSIZE - xThing, y*GRIDSIZE - yThing, GRIDSIZE, GRIDSIZE))
                else:
                    pygame.draw.rect(screen, NUMBACKGROUNDCOLOR, (x*GRIDSIZE -
                                     xThing, y*GRIDSIZE - yThing, GRIDSIZE, GRIDSIZE))
                    text = font.render(
                        str(xVal), True, (0, 0, 0), NUMBACKGROUNDCOLOR)
                    screen.blit(
                        text, (x*GRIDSIZE - xThing, y*GRIDSIZE - yThing))
                if trueX != xVal:
                    pygame.draw.rect(screen, FLAGCOLOR, (x*GRIDSIZE - xThing + GRIDSIZE //
                                     4, y*GRIDSIZE - yThing + GRIDSIZE//4, GRIDSIZE//2, GRIDSIZE//2))

         # create the grid
        for x in range(HEIGHT//GRIDSIZE + 1):
            pygame.draw.line(screen, (0, 0, 0), (0, x*GRIDSIZE -
                             yThing), (WIDTH, x*GRIDSIZE - yThing))
        for y in range(WIDTH//GRIDSIZE + 1):
            pygame.draw.line(screen, (0, 0, 0), (y*GRIDSIZE -
                             xThing, 0), (y*GRIDSIZE - xThing, HEIGHT))

        pygame.display.flip()

pygame.quit()
