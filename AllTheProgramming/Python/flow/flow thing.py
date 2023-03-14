import pygame
import pain

size = 5#only square boards bc not square make brain hurt
#points = [(0,0,'yellow'),(2,0,'orange'),(0,1,'red'),(4,2,'yellow'),(5,2,'orange'),(3,3,'red'),(4,3,'blue'),(5,3,'green'),(1,4,'green'),(0,5,'blue')]
points = [(4,0,'blue'),(3,2,'red'),(1,3,'yellow'),(3,3,'green'),(4,3,'yellow'),(1,4,'blue'),(2,4,'red'),(4,4,'green')]

pygame.init()
screen = pygame.display.set_mode([600,600])
running = True
hen = []
def getColor(color):
    rgb = ()
    if color == "red":
        rgb = (255,0,0)
    elif color == "blue":
        rgb = (0,0,255)
    elif color == "yellow":
        rgb = (255,255,0)
    elif color == "green":
        rgb = (0,255,0)
    elif color == "orange":
        rgb = (255,140,0)
    elif color == "darkBlue":
        rgb = (0,0,200)
    elif color == "pink":
        rgb = ()
    else:
        print("your an idoit")
        return "your a big stupid"
    return rgb
    
def drawDot(color,pos,size,screen):
    rgb = getColor(color)
    pygame.draw.circle(screen,rgb,pos,size)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((50,50,50))
    #render the thing
    scale = 600/size
    for e in range(size):
        pygame.draw.line(screen,(0,0,0),(0,e*scale),(600,e * scale))
        pygame.draw.line(screen,(0,0,0),(e*scale,0),(e * scale,600))
    for dot in points:
        drawDot(dot[2],(dot[0] * scale + scale/2,dot[1] * scale + scale/2),scale/2 - 10,screen)
    pygame.display.flip()
    hen = pain.pain(points,size)
    print("done")
    for e in hen:
        for pos in hen[e]:
            drawDot(e,(pos[0] * scale + scale/2, pos[1] * scale + scale / 2),10,screen)
    pygame.display.flip()
pygame.quit()
