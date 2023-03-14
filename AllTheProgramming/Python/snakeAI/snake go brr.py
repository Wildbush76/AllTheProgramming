import pygame
import random
import time
import copy
import TheFunnySnakeAi
pygame.init()
screen = pygame.display.set_mode([800,800])

class apple:
    def __init__(self):
        self.x = random.randint(0,19)
        self.y = random.randint(0,19)
        
    def render(self,screen):
        pygame.draw.rect(screen,(235,0,0),pygame.Rect(self.x*40,self.y*40,40,40))
    def makeNew(self,snakeBody):
        
        self.x = random.randint(0,19)
        self.y = random.randint(0,19)
        if [self.x,self.y] in snakeBody:
            self.makeNew(snakeBody)
class snake:
    def __init__(self,x,y,length):
        self.head = [x,y]
        self.body = []
        self.queue = []
        self.direction = 1
        self.path = []
        for xoffset in range(1,length):
            self.body.append([x-xoffset,y])
    def render(self,screen):
        pygame.draw.rect(screen,(0,200,0),pygame.Rect(self.head[0]*40,self.head[1]*40,40,40))
        for segment in self.body:
            pygame.draw.rect(screen,(30,230,30),pygame.Rect(segment[0]*40,segment[1]*40,40,40))
        for s in self.path:
            pygame.draw.rect(screen, (50,50,255),pygame.Rect(s[0] * 40,s[1] * 40,40,40))
    def move(self,app):
        if self.head == [app.x,app.y]:
            app.makeNew(self.body + self.head)
        else:
            self.body.pop()
        self.body.insert(0,copy.copy(self.head))
        #move thing yea
        if len(self.queue) > 0:
            self.direction = self.queue[0]
            self.queue = self.queue[1:]
            if len(self.path) > 0:
                self.path.pop(0)
        else:
            e = TheFunnySnakeAi.Astar(20,20,self,app,False)
            cords = []
            if type(e) == str:
                print(e)
                self.render(screen)
                app.render(screen)
                pygame.display.flip()
                input()
                return
            #cords.insert(0,self.head)
            while e != None:
                cords.insert(0,[e.x,e.y])
                e = e.previous
            self.path = cords[2:-1]
            for cord in range(len(cords)):
                if cord < len(cords)-1:
                    if cords[cord][0] - cords[cord + 1][0] == 1:
                        self.queue.append(3)
                    elif cords[cord][0] - cords[cord + 1][0] == -1:
                        self.queue.append(1)
                    elif cords[cord][1] - cords[cord + 1][1] == 1:
                        self.queue.append(4)
                    elif cords[cord][1] - cords[cord + 1][1] == -1:
                        self.queue.append(2)
            if len(self.queue) > 0:
                self.direction = self.queue[0]
                self.queue = self.queue[1:]
            else:
                print("i dont really know what happend but alright then")
        
        if self.direction == 1:
            self.head[0] += 1
        elif self.direction == 2:
            self.head[1] += 1
        elif self.direction == 3:
            self.head[0] -= 1
        else:
            self.head[1] -= 1
snakeMan = snake(10,10,5)
app = apple()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((200,200,200))
    snakeMan.render(screen)
    snakeMan.move(app)
    app.render(screen)
    pygame.display.flip()
    #time.sleep(0.1)
pygame.quit()
#amongus
