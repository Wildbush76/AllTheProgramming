import pygame
import numpy as np
import math
import time
from PIL import Image, ImageOps
class pix:
    def __init__(self,pos,value):
        self.y = pos[0]
        self.x = pos[1]
        self.value = value
        self.number = 0
    def findN(self,pixels,width,height,outline):
        amount = 0
        if self.value == 255:
            return
        if self.x > 0:
            if pixels[self.y][self.x - 1].value == 0:
                amount += 1
       
        if self.x < width-1:
            if pixels[self.y][self.x + 1].value == 0:
                amount += 1
      
        if self.y > 0:
            if pixels[self.y - 1][self.x].value == 0:
                amount +=1
            if self.x > 0:
                if pixels[self.y - 1][self.x - 1].value == 0:
                    amount += 1
            if self.x < width-1:
                if pixels[self.y - 1][self.x + 1].value == 0:
                    amount += 1
        if self.y < height-1:
            if pixels[self.y + 1][self.x].value == 0:
                amount+=1
            if self.x > 0:
                if pixels[self.y + 1][self.x - 1].value == 0:
                    amount += 1
            if self.x < width-1:
                if pixels[self.y + 1][self.x + 1].value == 0:
                    amount += 1
        self.number = amount
        if amount < 8:
            outline.append([self.x * (220/width),self.y * (220/height)])
            return True
        return False
def isNear(pos1,pos2):
    return (pos1[0]-pos2[0])**2 + (pos1[1] - pos2[1])**2
            
        
photo = ImageOps.grayscale(Image.open("asdf.jfif"))
pixels = np.array(photo.getdata())
#convert to only black and white

#convert to 2d array
width,height = photo.size
data = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(pix([y,x],round(pixels[y * width + x]/255)*255))
    data.append(row)
print("made list")
#find the amount of neightbors
outline = []

for y in data:
    for x in y:
        x.findN(data,width,height,outline)
    
#create the outline
newOutLine = []
targetLength = len(outline)
current = outline[0]
outline = outline
while len(newOutLine) != targetLength:
    distances = []
    for p in outline:
       distances.append((p,isNear(current,p)))
    distances = sorted(distances,key = lambda x : x[1])
    theOne = distances[0][0]
    current = theOne
    if distances[0][1] > 4:
        newOutLine.append((theOne,"T"))
    else:
        newOutLine.append((theOne,"D"))
    #outline.remove(theOne)
        outline.remove(theOne)
#try to fill in the shape
L = newOutLine[0][0][1]
U = L
for x in newOutLine:
    if x[0][1] < L:
        L = x[0][1]
    elif x[0][1] > U:
        U = x[0][1]
#save Gcode
with open("test.gcode","a") as file:
    file.write("G28\nG29\nG1 Z0")
    up = False
    for x in newOutLine:
        if x[1] == "D":
            file.write(f"G1 X{x[0][0]} Y{x[0][1]}\n")
        else:
            file.write("G0 Z1\n")
            file.write(f"G0 F6000 X{x[0][0]} Y{x[0][1]}\n")
            file.write("G0 Z0")
            
#display the points for debugging
pygame.init()
screen = pygame.display.set_mode([440,440])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    for x in range(1,len(newOutLine)):
        #pygame.draw.circle(screen,(0,0,255),(x[0],x[1]),1)
        color = (0,0,255)
        if newOutLine[x][1] == "T":
            color = (0,255,0)
        pygame.draw.line(screen,color,(newOutLine[x-1][0][0]*2,newOutLine[x-1][0][1]*2),(newOutLine[x][0][0]*2,newOutLine[x][0][1]*2),1)
        #pygame.display.flip()
        #time.sleep(0.1)
        
    pygame.display.flip()   
pygame.quit()
