import pygame
import math

pygame.init()

WIDTH = 500
HEIGHT = 500
DISTANCE = 30
RADIUS = 50

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True

class bullet:
    pass

class turret:
    def __init__(self,x,y,radius = 50):
        self.x = x
        self.y = y
        self.angle = 0
        self.targetAngle = 0
        self.radius = radius
    def do(self,screen,targetX,targetY):
        self.targetAngle = math.atan2(targetY-self.y,targetX-self.x)
        if abs(self.angle - self.targetAngle) < abs(3.14- self.targetAngle - self.angle):
            self.angle += 0.01
        else:
            self.angle -= 0.01

        xAim = math.cos(self.angle)
        yAmin = math.sin(self.angle)
        pygame.draw.circle(screen,(0,200,0),(self.x,self.y),self.radius)
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x + xAim*RADIUS, self.y + yAmin *RADIUS),5)

        

yea = turret(WIDTH//2,HEIGHT//2)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    mpos = pygame.mouse.get_pos()

    yea.do(screen,mpos[0],mpos[1])
    #turret time
    
    pygame.display.flip()

pygame.quit()