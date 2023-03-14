import pygame
import math
import time
pygame.init()

screen = pygame.display.set_mode([600,600])

running = True

class cube:
    def __init__(self):
        self.lines = []
        self.offsets = {'x':0,'y':0,'z':0}
        self.draw()
    def offset(self,pt,offset):
        angle = math.degrees(math.atan((pt[1]-300)/(pt[0]-300))) + offset
        distance = math.sqrt(((pt[0]-300)**2) + ((pt[1]-300)**2))
        return [round(math.sin(math.radians(angle)) * distance + 300), round(math.cos(math.radians(angle)) * distance + 300)]
    def apply(self):
        #apply x
        for l in self.lines:
            for line in l:
                pt = self.offset([line[0],line[2]],self.offsets['x'])
                
                line[0] = pt[0]
                line[2] = pt[1]
        #apply y
        for l in self.lines:
            for line in l:
                pt = self.offset([line[1],line[2]],self.offsets['y'])
                line[1] = pt[0]
                line[2] = pt[1]
                
                
        
    def draw(self,screen = False):
        self.lines = []#ill do this later ig
        prev = []
        for a in range(45,495,90):
            x = round(math.sin(math.radians(a + self.offsets['z'])) * math.sqrt(2)*100 + 300)
            y = round(math.cos(math.radians(a + self.offsets['z'])) * math.sqrt(2)*100 + 300)
            self.lines.append([[x,y,400],[x,y,200]])
            if len(prev) > 0:
                self.lines.append([[prev[0],prev[1],400],[x,y,400]])
                self.lines.append([[prev[0],prev[1],200],[x,y,200]])
            prev = [x,y]
        self.apply()
        if screen != False:
            for l in self.lines:
                pygame.draw.line(screen,(0,0,0),l[0][:-1],l[1][:-1])
            pygame.display.flip()
angle = 0;
test = cube()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255,255,255))
    test.draw(screen)
    test.offsets['y'] += 1
    test.offsets['x'] += 1
    #print(len(test.lines))
    #for x in test.lines:
       # print(x)
   # input()
    time.sleep(0.1)
    
pygame.quit()
