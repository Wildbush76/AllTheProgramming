from PIL import Image
import math

THRESHOLD_VALUE = 100
NOISE_REDUCTION = 0#higher number lower the noise in a way, or might just delete small shapes....

SIZE = 150#mm
OFFSET = (100,100)#mm

def floodFill(x : int,y : int,pixels : list) -> None:
    queue = [[x,y]]
    def addToTheQueue(cords : list):
        if cords not in queue:
            queue.append(cords)
    while len(queue) > 0:
        n = queue.pop(0)
        pixels[n[1]][n[0]] = 2
        x,y = n
        if n[0] > 0:
            if pixels[n[1]][n[0] - 1] == 0:
                addToTheQueue([n[0] - 1,n[1]])
            if y > 0 and pixels[n[1] - 1][n[0] - 1] == 0:
                addToTheQueue([n[0] - 1,n[1] - 1])
            if y < len(pixels) - 1 and pixels[n[1] + 1][n[0] - 1] == 0:
                addToTheQueue([n[0] - 1,n[1] + 1])

        if n[0] < len(pixels[0]) - 1:
            if pixels[n[1]][n[0] + 1] == 0:
                addToTheQueue([n[0] + 1,n[1]])
            if n[1] > 0 and pixels[n[1] - 1][n[0] + 1] == 0:
                addToTheQueue([n[0] + 1,n[1] - 1])
            if y < len(pixels) - 1 and pixels[n[1] + 1][n[0] + 1] == 0:
                addToTheQueue([n[0] + 1,n[1] + 1])

        if n[1] > 0 and pixels[n[1] - 1][n[0]] == 0:
            addToTheQueue([n[0],n[1] - 1])
        if n[1] < len(pixels) - 1 and pixels[n[1] + 1][n[0]] == 0:
            addToTheQueue([n[0],n[1] + 1])



def amIAnEdge(x : int, y : int, pixels : list) -> bool:
    if y > 0:
        if pixels[y - 1][x] == 2:
            return True
        if x > 0 and pixels[y - 1][x - 1] == 2:
            return True
        if x < len(pixels[0]) - 1 and pixels[y - 1][x + 1] == 2:
            return True
    if y < len(pixels) - 1:
        if pixels[y + 1][x] == 2:
            return True
        if x > 0 and pixels[y + 1][x - 1] == 2:
            return True
        if x < len(pixels[0]) - 1 and pixels[y + 1][x + 1] == 2:
            return True

    if x > 0 and pixels[y][x - 1] == 2:
        return True
    if x < len(pixels[0]) - 1 and pixels[y][x + 1] == 2:
        return True
    return False


def findShape(x : int, y : int, pixels : list) -> list:
    shape = []
    added = True
    pixels[y][x] = 0
    while added:
        added = False
        shape.append([x,y])
        
        if x > 0 and pixels[y][x - 1] == 1:
            pixels[y][x - 1] = 0
            x -= 1
            added = True
        elif x < len(pixels[0]) -1 and  pixels[y][x + 1] == 1:
            pixels[y][x + 1] = 0
            x += 1
            added = True
        elif y > 0 and  pixels[y - 1][x] == 1:
            pixels[y - 1][x] = 0
            y -= 1
            added = True
        elif y < len(pixels)-1 and  pixels[y + 1][x] == 1:
            pixels[y + 1][x] = 0
            y+= 1
            added = True
        elif y > 0 and x > 0 and pixels[y - 1][x - 1] == 1:
            pixels[y - 1][x - 1] = 0
            y -= 1
            x -= 1
            added = True
        elif y < len(pixels) - 1 and x > 0 and pixels[y + 1][x - 1] == 1:
            pixels[y + 1][x - 1] = 0
            y += 1
            x -= 1
            added = True
        elif y < len(pixels) - 1 and x < len(pixels[0]) - 1 and pixels[y + 1][x + 1] == 1:
            pixels[y + 1][x + 1] = 0
            y += 1
            x += 1
            added = True
        elif y > 0 and x < len(pixels[0]) - 1 and pixels[y - 1][x + 1] == 1:
            pixels[y - 1][x + 1] = 0
            y -= 1
            x += 1
            added = True
  

    floodFill(x,y,pixels)
    return shape


def main(image : str):
    print("loading image...")
    try:
        img = Image.open(image,"r")
    except FileNotFoundError as e:
        print("image not found")
        return
    pixelValues = list(img.getdata())
    WIDTH, HEIGHT = img.size
    SCALE = SIZE/max(WIDTH,HEIGHT)
    grid = []

    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            pixel = pixelValues[y * WIDTH  + x]
            if hasattr(pixel, '__iter__'):
                if len(pixel) > 3 and pixel[-1] == 0:
                    row.append(2)
                    continue
                grayScaleValue = sum(pixel[:3])/3
            else:
               grayScaleValue = pixel
            if grayScaleValue > THRESHOLD_VALUE:#2 white, 1 edge, 0 black
                row.append(2)
            else:
                row.append(0)
        grid.append(row)
   
    print("isolating edges...")
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] != 2:
                if amIAnEdge(x,y,grid):
                    grid[y][x] = 1
    print("detecting shapes...")
    shapes = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] == 1:
                shapes.append(findShape(x,y,grid))
    print(f"{len(shapes)} shapes detected")

    print("refining shapes...")
   
    for shapeIndex in range(len(shapes)):
        refinedShape = []
        previousPoint = shapes[shapeIndex][-1]
        shapes[shapeIndex] = list(map(lambda p: (p[0] * SCALE + OFFSET[0], p[1]* SCALE + OFFSET[1]),shapes[shapeIndex]))
        for point in shapes[shapeIndex]:
            if math.dist(point,previousPoint) >= NOISE_REDUCTION:
                refinedShape.append((point[0],point[1]))
                previousPoint = point
        shapes[shapeIndex] = refinedShape
    print("generating paths...")

    shapes = [x for x in shapes if len(x) > 1]

    with open(f"{'.'.join(image.split('.')[:-1])}.gcode","w") as file:
        output = ["G28 X Y R0","G0 F5000","G F500"]

        for shape in shapes:
            output.append("G0 Z5")
            output.append(f"G0 X%.3f Y%.3f"%(shape[0][0],shape[0][1]))
            output.append("G1 Z0")

            for point in shape:
                output.append(f"G1  X%.3f Y%.3f"%(point[0],point[1]))
            if math.dist(shape[0],shape[-1]) > 5:
                output.pop(-1)
        file.write("\n".join(output))
    print("paths generated!")

if __name__ == "__main__":
    main(r"C:\Users\wildb\Desktop\ImageToLien\thisBreaksMyCode.png")