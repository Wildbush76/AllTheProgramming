import math

def Astar(boardX,boardY,snake,app, long):
    openSet = []
    closedSet = []
    path = []

    def heu(a,b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    class node:
        def __init__(self,x,y,snake):
            self.x = x
            self.y = y
            self.f = 0
            self.g = 0
            self.h = 0
            self.Nei = []
            self.wall = False
            self.path = 0
            if [self.x,self.y] in snake.body or ([self.x,self.y] == snake.head):
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
            collum.append(node(x,y,snake))
        grid.append(collum)
    for y in range(boardX):
        for x in range(boardY):
            grid[y][x].findNei(grid)
    openSet.append(grid[snake.head[1]][snake.head[0]])
    openSet[0].previous = None
    end = grid[app.y][app.x]
   
    
    #yes time
    while len(openSet) > 0:
        lowest = 0
        for e in openSet:
            if (e.f < openSet[lowest].f and not long) or (e.f > openSet[lowest].f and long):
                lowest = openSet.index(e)
        current = openSet[lowest]
        if current == end:
            #add stuff later
            return current
        openSet.remove(current)
        closedSet.append(current)
        neighbors = current.Nei
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            length = []
            t = current
            while t != None:
                length.append(t)
                t = t.previous
            if len(snake.body) > 20:
                reachable = FloodFill(boardX,boardY,list(map(lambda x : [x.x,x.y],length[:len(snake.body)])),[current.x,current.y])
            else:
                reachable = 1
            if neighbor not in closedSet and (not neighbor.wall or len(length) > len(snake.body)) and reachable > 0.7:
                tempg = current.g + 1
                if neighbor in openSet:
                    if (tempg < neighbor.g and not long) or (tempg > neighbor.g and long):
                        neighbor.g = tempg
                else:
                    neighbor.g = tempg
                    openSet.append(neighbor)
                neighbor.h = heu([neighbor.x,neighbor.y],[end.x,end.y])
                neighbor.f = neighbor.g + neighbor.h
                current.path += 1
                neighbor.previous = current
    if not long:
        print("why dont we try something new")
        return Astar(boardX,boardY,snake,app, True)
    print(f"your long {len(snake.body)}")
    return "oh lord something is wrong"
    
def FloodFill(boardX,boardY,walls,point):
    theOnes = [point]
    searching = [point]
    while len(searching) > 0:
        q = searching[0]
        searching.pop(0)
        if q[0] > 0:
            if [q[0] - 1, q[1]] not in walls and [q[0] - 1, q[1]] not in theOnes:
                searching.append([q[0] - 1, q[1]])
                theOnes.append([q[0] - 1, q[1]])
        if q[0] < boardX - 1:
            if [q[0] + 1, q[1]] not in walls and [q[0] + 1, q[1]] not in theOnes:
                searching.append([q[0] + 1, q[1]])
                theOnes.append([q[0] + 1, q[1]])
        if q[1] > 0:
            if [q[0], q[1] - 1] not in walls and [q[0], q[1] - 1] not in theOnes:
                searching.append([q[0], q[1] - 1])
                theOnes.append([q[0], q[1] - 1])
        if q[1] < boardY -1:
            if [q[0], q[1] + 1] not in walls and [q[0], q[1] + 1] not in theOnes:
                searching.append([q[0], q[1] + 1])
                theOnes.append([q[0], q[1] + 1])
    return len(theOnes)/(boardX*boardY)       
