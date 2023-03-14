#suffering
import Yo_its_Astar as Astar
def pain(points,size):

    paths = {}
    for dot in points:
        if dot[2] not in paths:
            paths[dot[2]] = [dot[:2]]
        else:
            paths[dot[2]].append(dot[:2])
            paths[dot[2]].append([])
   
    #paths = dict => [[x,y],[x,y],paths]
    walls = []
    theOne = 0
    colors = [x for x in  paths]
    while True:
        if theOne >= len(colors):
            break
        otherPoints = []
        for e in paths:
            if e != colors[theOne]:
                print(paths[e])
                print(e)
                otherPoints.append(list(paths[e][0]))#why doesnt it just work 
                otherPoints.append(list(paths[e][1]))#programming is going to be the death of me
        lol = Astar.Astar(size,size,paths[colors[theOne]][0],walls + otherPoints,paths[colors[theOne]][1],paths[colors[theOne]][2])
        if lol != None:
            walls += lol[1:]
            paths[colors[theOne]][2].append(lol[1:])
            theOne += 1
        else:
            #print("wat this isnt the right")#AHHHHHH so many print statements
            if theOne > 0:
                paths[colors[theOne]][2] = []
                theOne -= 1
                walls = walls[:-len(paths[colors[theOne]][2][-1])]
            else:
                raise Exception("your idoit")
        #print("\n" + "-"*50)
    final = {}
    for e in paths:
        final[e] = paths[e][2][-1]
    return final
    pass
