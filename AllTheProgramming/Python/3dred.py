import math
#import pygame
import pygame
class player:
    def __init__(self,x,y,fov,direction):
        self.x = x
        self.y = y
        self.fov = fov//2
        self.direction = direction
        self.detail = 60
    def render(self,screen,TheMap):
        #body
        pygame.draw.circle(screen,(150,0,0),(self.x,self.y),10)
        #fov
        angle = math.radians(self.direction - self.fov)
        lines = ((math.cos(angle)*1000 + self.x,math.sin(math.radians(self.direction - self.fov))*1000 + self.y),(math.cos(angle)*1000 + self.x,math.sin(angle + self.fov)*1000 + self.y))
        pygame.draw.line(screen,(0,0,200),(self.x,self.y),(lines[0][0],lines[0][1]))
        angle += math.radians(self.fov*2)
        pygame.draw.line(screen,(0,0,200),(self.x,self.y),(lines[1][0],lines[1][0]))
        #big dumb math
        points = []
        
        for line in lines:
            slope = (line[1] - self.y) / (line[0] - self.x)
            intercept = self.y - (slope * self.x)
            closest = [0,0,10000000]
            for square in TheMap:
                sides = (('x',square[0]),('x',square[0] + 50), ('y',square[1]),('y',square[1] + 50))
                for side in sides:
                    if side[0] == "x":
                        interceptPoint = side[1] * slope + intercept
                        if interceptPoint >= square[1] and interceptPoint <= square[1] + 50:
                            distance = math.sqrt((self.x - side[1]) ** 2 + (self.y - interceptPoint) ** 2)
                            if distance < closest[2]:
                                closest = [side[1],interceptPoint,distance]
                    else:
                        interceptPoint = (side[1] - intercept)/slope
                        if interceptPoint >= square[0] and interceptPoint <= square[0] + 50:
                            distance = math.sqrt((self.x - interceptPoint) ** 2 + (self.y - side[1]) ** 2)
                            if distance < closest[2]:
                                closest = [interceptPoint,side[1],distance]
            pygame.draw.circle(screen,(255,0,0), (closest[1],closest[2]),5)
                            
pygame.init()
screen = pygame.display.set_mode([700,700])
running = True
TheMap = []
with open("MAP.txt","r") as file:
    data = file.read().split("\n")
    if len(data) != 14 or len(data[0]) != 14:
        pygame.quit()
        print("MAP SIZE WRONG")
        raise Exception("Incorrect map size")
    for y in range(len(data)):
        for x in range(len(data[y])):
            if int(data[y][x]) == 1:
                TheMap.append((x * 50,y * 50))
MainPlayer = player(100,100,60,0)
TheMap = tuple(TheMap)
keys = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys.append(event.key)
        elif event.type == pygame.KEYUP:
            try:
                keys.remove(event.key)
            except:
                pass
    screen.fill((255,255,255))
    if pygame.K_w in keys:
        MainPlayer.y -= 1
    elif pygame.K_s in keys:
        MainPlayer.y += 1
    if pygame.K_a in keys:
        MainPlayer.x -= 1
    elif pygame.K_d in keys:
        MainPlayer.x += 1
    #dugbug
    MainPlayer.render(screen,TheMap)
    for spot in TheMap:
        pygame.draw.rect(screen,(100,100,100),pygame.Rect(spot[0],spot[1],50,50))
    pygame.display.flip()
pygame.quit()
