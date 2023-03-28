# restarting because im stupid
import math
import random
import serial

PORT = "COM5"
BUADRATE = 115200

try:
    ser = serial.Serial(PORT, BUADRATE)
except Exception as e:
    pass
    # exit("Printer not found on serial port")

PRINTBED = (180, 180)

NUMBEROFMINES = 10

XOFFSET = 20
YOFFSET = 20

FEEDSPEED = 1200

SIZE = 20

HOTENDTEMP = 210
BEDTEMP = 60

# e steps per millimeter you stupid idiots
ESTEPSPERMM = 0.4

GRIDSIZE = min(*PRINTBED)//SIZE
NUMBERMARGINS = 2  # area around the numbers and flags and shit

RETRACT = 14

with open("numbers.txt", "r") as file:
    NUMBERS = eval(file.read().replace("\n", ""))


class block:
    def __init__(self, x: int, y: int, mine: bool):
        self.x = x
        self.y = y
        self.mine = mine
        if self.mine:
            self.n = 9
        else:
            self.n = 0
        self.shown = False

    def show(self, outputCode: list, currentPos: list, currentE: float) -> float:
        if self.mine == True:
            print("your simply bad")
            exit()
        if self.shown:
            print("its already showing you")
            return currentE
        self.shown = True

        # travel(*currentPos, outputCode)

        currentE = self.doDaMovement(
            NUMBERS[self.n], outputCode, currentPos, currentE)
        return currentE

    def doDaMovement(self, theMovement: list, outputCode: list, currentPos: list, currentE: float) -> float:
        bottomLeft = [self.x * SIZE + XOFFSET, self.y * SIZE + YOFFSET]
        for movement in theMovement:
            numberSize = (SIZE - NUMBERMARGINS*2)
            startX = movement[0] * numberSize + bottomLeft[0] + NUMBERMARGINS
            startY = movement[1] * numberSize + bottomLeft[1] + NUMBERMARGINS
            endX = movement[2] * numberSize + bottomLeft[0] + NUMBERMARGINS
            endY = movement[3] * numberSize + bottomLeft[1] + NUMBERMARGINS
            currentE += getDistance(startX, startY, endX, endY) * ESTEPSPERMM
            if startX != currentPos[0] or startY != currentPos[1]:
                travel(startX, startY, outputCode, currentE)
            line(currentE, endX, endY, outputCode)
            currentPos = [endX, endY]
        return currentE

    def flag(self, outputCode: list, currentPos: list, currentE: float):
        return self.doDaMovement(NUMBERS[9], outputCode, currentPos, currentE)

    def getNeighbors(self, grid: list) -> None:
        if self.mine:
            self.n = 9
            return
        if self.x > 0:
            if grid[self.y][self.x - 1].mine:
                self.n += 1
            if self.y > 0 and grid[self.y - 1][self.x - 1].mine:
                self.n += 1
            if self.y < len(grid) - 1 and grid[self.y + 1][self.x - 1].mine:
                self.n += 1
        if self.x < len(grid[0]) - 1:
            if grid[self.y][self.x + 1].mine:
                self.n += 1
            if self.y > 0 and grid[self.y - 1][self.x + 1].mine:
                self.n += 1
            if self.y < len(grid) - 1 and grid[self.y + 1][self.x + 1].mine:
                self.n += 1
        if self.y > 0 and grid[self.y - 1][self.x].mine:
            self.n += 1
        if self.y < len(grid) - 1 and grid[self.y + 1][self.x].mine:
            self.n += 1


def applyFL(grid: list, x: int, y: int, outputCode: list, currentPos: list, currentE: float) -> float:
    if grid[y][x].shown or grid[y][x].mine:
        return currentE
    currentE = grid[y][x].show(outputCode, currentPos, currentE)
    if grid[y][x].n != 0:
        return currentE
    return funnyFloodFill(grid, x, y, outputCode, currentPos, currentE)


def funnyFloodFill(grid: list, x: int, y: int, outputCode: list, currentPos: list, currentE: float) -> float:
    if x > 0:
        currentE = applyFL(grid, x - 1, y, outputCode, currentPos, currentE)
        if y > 0:
            currentE = applyFL(grid, x - 1, y - 1,
                               outputCode, currentPos, currentE)
        if y < len(grid) - 1:
            currentE = applyFL(grid, x - 1, y + 1,
                               outputCode, currentPos, currentE)
    if x < len(grid[0]) - 1:
        currentE = applyFL(grid, x + 1, y, outputCode, currentPos, currentE)
        if y > 0:
            currentE = applyFL(grid, x + 1, y - 1,
                               outputCode, currentPos, currentE)
        if y < len(grid) - 1:
            currentE = applyFL(grid, x + 1, y + 1,
                               outputCode, currentPos, currentE)
    if y > 0:
        currentE = applyFL(grid, x, y - 1, outputCode, currentPos, currentE)
    if y < len(grid) - 1:
        currentE = applyFL(grid, x, y + 1, outputCode, currentPos, currentE)
    return currentE


def travel(targetX: float, targetY: float, output: list, currentE: float) -> None:
    # maybe add some retraction later, who knows
    output.append(f"G0 Z1 E{currentE - RETRACT}")
    output.append(f"G0 F5000 X{targetX} Y{targetY}")
    output.append(f"G0 F{FEEDSPEED} E{currentE} Z0")


def line(E: float, targetX: float, targetY: float, output: list) -> None:
    output.append(f"G1 X{targetX} Y{targetY} E{E}")


def getDistance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


currentE = 0
outputCode = [f"M104 S{HOTENDTEMP}",
              f"M140 S{BEDTEMP}", "M109", "G28 X Y R0", "M82", "G92", "M107", "M208 F1500", f"G1 F{FEEDSPEED}", "M117 moving", "M118 P0", "M105"]

# create a grid ig?
currentPos = [0, 0]

for vertLines in range(XOFFSET, GRIDSIZE * SIZE + XOFFSET + SIZE, SIZE):
    currentPos = [vertLines, YOFFSET]
    travel(*currentPos, outputCode, currentE)
    x = GRIDSIZE * SIZE + YOFFSET
    currentE += getDistance(*currentPos, vertLines, x) * ESTEPSPERMM
    line(currentE, vertLines, GRIDSIZE*SIZE + YOFFSET, outputCode)

for horiLines in range(YOFFSET, GRIDSIZE * SIZE + YOFFSET + SIZE, SIZE):
    currentPos = [XOFFSET, horiLines]
    travel(*currentPos, outputCode, currentE)
    y = GRIDSIZE * SIZE + XOFFSET
    currentE += getDistance(*currentPos, y, horiLines) * ESTEPSPERMM
    line(currentE, y, horiLines, outputCode)

mines = []
while (len(mines) < NUMBEROFMINES):
    pos = [random.randint(0, GRIDSIZE), random.randint(0, GRIDSIZE)]
    if pos not in mines:
        mines.append(pos)
grid = []
for y in range(GRIDSIZE):
    row = []
    for x in range(GRIDSIZE):
        if [x, y] in mines:
            row.append(block(x, y, True))
            mines.remove([x, y])
        else:
            row.append(block(x, y, False))
    grid.append(row)

for row in grid:
    for thing in row:
        thing.getNeighbors(grid)

while True:
    print("-"*50)
    doing = input("make a move stupid : ").split(",")  # x,y,doing
    doing[0] = int(doing[0])
    doing[1] = int(doing[1])
    if max(*doing[0:2]) > SIZE:
        print("no, bad thats not within size, don't.. don't do that.. pwease")
        continue

    if len(doing) <= 2 or doing[2] == "C":
        currentE = grid[int(doing[1])][int(doing[0])].show(
            outputCode, currentPos, currentE)
        currentE = funnyFloodFill(grid, int(doing[1]), int(
            doing[0]), outputCode, currentPos, currentE)
    else:
        currentE = grid[int(doing[1])][int(doing[0])].flag(
            outputCode, currentPos, currentE)
    for command in outputCode:
        command += "\n"
        ser.write(command.encode())
        print(f"Sending {command}", end="")
        data = ""
        while ("ok" not in data):
            data = str(ser.readline().strip())
    outputCode = []
# hehed
