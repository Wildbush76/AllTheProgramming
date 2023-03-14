from enum import auto
import pygame
import math
pygame.init()

screen = pygame.display.set_mode([600,600])
class sphere:
    def __init__(self,size,x,y,M = 40, N = 40):
        self.lat = []
        self.origin = [x,y]
        self.long = []
        self.size = size
        self.rotatations = {'x':0,'y':0,'z':0}
        for m in range(M + 1):
            asd = []
            for n in range(N + 1):
                x = round(math.sin(math.pi * m/M) * math.cos(2*math.pi * n/N) * size)
                y = round(math.sin(math.pi * m/M) * math.sin(2*math.pi * n/N) * size)
                z = round(math.cos(math.pi * m/M) * size)
                #self.points.append([x,y,z])
                asd.append([x,y,z])
            self.long.append(asd)
        for n in range(N + 1):
            asd = []
            for m in range(M + 1):
                x = round(math.sin(math.pi * m/M) * math.cos(2*math.pi * n/N) * size)
                y = round(math.sin(math.pi * m/M) * math.sin(2*math.pi * n/N) * size)
                z = round(math.cos(math.pi * m/M) * size)
                #self.points.append([x,y,z])
                asd.append([x,y,z])
            self.lat.append(asd)
                
    def draw(self,screen):
        for long in self.long:
            prev = [long[-1][0] + self.origin[0],long[-1][1] + self.origin[1]]
            for points in long:
                x = points[0] + self.origin[0]
                y = points[1] + self.origin[1]
                pygame.draw.line(screen,(0,0,0),prev,[x,y])
                prev = [x,y]
        for long in self.lat:
            prev = [long[-1][0] + self.origin[0],long[-1][1] + self.origin[1]]
            for points in long:
                x = points[0] + self.origin[0]
                y = points[1] + self.origin[1]
                                
                
                pygame.draw.line(screen,(0,0,0),prev,[x,y])
                prev = [x,y]
    def rotateZ(self,a):
        a = math.radians(a)
        sinT = math.sin(a)
        cosT = math.cos(a)
        for l in self.long:
            for long in l:
                x = long[0] * cosT - long[1] * sinT
                y = long[1] * cosT + long[0] * sinT
                long[0] = x
                long[1] = y
        for l in self.lat:
            for long in l:
                x = long[0] * cosT - long[1] * sinT
                y = long[1] * cosT + long[0] * sinT
                long[0] = x
                long[1] = y
    def rotateX(self,a):
        a = math.radians(a)
        sinT = math.sin(a)
        cosT = math.cos(a)
        for l in self.long:
            for long in l:
                x = long[2] * cosT - long[1] * sinT
                y = long[1] * cosT + long[2] * sinT
                long[2] = x
                long[1] = y
        for l in self.lat:
            for long in l:
                x = long[2] * cosT - long[1] * sinT
                y = long[1] * cosT + long[2] * sinT
                long[2] = x
                long[1] = y
    def rotateY(self,a):
        a = math.radians(a)
        sinT = math.sin(a)
        cosT = math.cos(a)
        for l in self.long:
            for long in l:
                x = long[0] * cosT - long[2] * sinT
                y = long[2] * cosT + long[0] * sinT
                long[0] = x
                long[2] = y
        for l in self.lat:
            for long in l:
                x = long[0] * cosT - long[2] * sinT
                y = long[2] * cosT + long[0] * sinT
                long[0] = x
                long[2] = y
yea = sphere(100,300,300,20,20)
running = True
orin = [0,0]
#m = list(pyautogui.position())
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    yea.draw(screen)
    yea.rotateY(0.1)
    yea.rotateX(-0.2)
   
    #anglx = list(pyautogui.position())
    #anglx[0] = (anglx[0]/1919) * 360
    #anglx[1] = (anglx[1]/1079) * 360
    #yea.rotateY(orin[0] - anglx[0])
    #yea.rotateX(orin[1] - anglx[1])    
    #orin = anglx

    pygame.display.flip()

    
pygame.quit()
