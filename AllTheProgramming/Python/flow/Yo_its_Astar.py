import math

def Astar(boardX,boardY,start,walls,stop,past):
    openSet = []
    closedSet = []
    path = []

    def heu(a,b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    class node:
        def __init__(self,x,y,walls,start):
            self.x = x
            self.y = y
            self.f = 0
            self.g = 0
            self.h = 0
            self.Nei = []
            self.wall = False
            self.path = 0
            if [self.x,self.y] in walls or [self.x,self.y] == start:
                self.wall = True
        def findNei(self,grid):
            if self.x < boardX-1:
                self.Nei.append(grid[self.y][self.x + 1])
            if self.x > 0:
                self.Nei.append(grid[self.y][self.x - 1])
            if self.y < boardY-1:
                self.Nei.append(grid[self.y + 1][self.x])
            if self.y > 0:
                self.Nei.append(grid[self.y - 1][self.x])
    grid = []
    for y in range(boardX):
        collum = []
        for x in range(boardY):
            collum.append(node(x,y,walls,start))
        grid.append(collum)
    for y in range(boardX):
        for x in range(boardY):
            grid[y][x].findNei(grid)
    openSet.append(grid[start[1]][start[0]])
    openSet[0].previous = None
    end = grid[stop[1]][stop[0]]
   
    
    #yes time
    while len(openSet) > 0:
        lowest = 0
        for e in openSet:
            if (e.f < openSet[lowest].f):
                lowest = openSet.index(e)
        current = openSet[lowest]
        if current == end:
            #add stuff later
            path = []
            e = current
            while e.previous != None:
                path.append([e.x,e.y])
                e = e.previous
                
            return path
        openSet.remove(current)
        closedSet.append(current)
        neighbors = current.Nei
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            length = []
            t = current
            while t.previous != None:
                length.append([t.x,t.y])
                t = t.previous
            canWeDoIt = True#lol no we cant
            if len(past) > 0:
                if len(length) == len(past[0]):
                    if length in past:
                        canWeDoIt = False
           
            if neighbor not in closedSet and not neighbor.wall and canWeDoIt:
                tempg = current.g + 1
                if neighbor in openSet:
                    if (tempg < neighbor.g):
                        neighbor.g = tempg
                else:
                    neighbor.g = tempg
                    openSet.append(neighbor)
                neighbor.h = heu([neighbor.x,neighbor.y],[end.x,end.y])
                neighbor.f = neighbor.g + neighbor.h

                neighbor.previous = current
    return None
