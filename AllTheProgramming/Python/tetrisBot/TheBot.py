from PIL import ImageGrab, ImageOps
import time
import math
from copy import deepcopy
import keyboard
#import mouse #i want to move scren, just comment if no like
import numpy as np
bboxthing = [1186,242,1426,722] #please put the bbox coords here k thnx
clicks = 1
held = ["null"]
def GetState(info):
    board = []
    
    ScreenShot = ImageOps.grayscale(ImageGrab.grab(bbox=(bboxthing[0],bboxthing[1],bboxthing[2],bboxthing[3])))# old is 306,173,546,653
    #ScreenShot.save("test.png")#not needed unless testing
    pixels = ScreenShot.getdata()
    for y in range(12,480,24):
        row = []
        for x in range(12,240,24):
          
            pixel = np.array(pixels[x + (y * 240)])
            if pixel in [131,92,120,1611,79,122,71,61,161]:
                row.append("0")
            else:
                row.append("#")
            if pixel in [59,46,35,39,60,80,65]:
                
                if pixel == 65:
                    info.append([1,[[0, 1], [1, 0], [1, 1], [2, 0]]])
                elif pixel == 39:
                    info.append([2,[[0, 0], [1, 0], [1, 1], [2, 1]]])
                elif pixel == 46:
                    info.append([3,[[0, 1], [1, 0], [1, 1], [2, 1]]])
                elif pixel == 80:
                    info.append([4,[[0, 0], [0, 1], [1, 0], [1, 1]]])
                elif pixel == 59:
                    info.append([5,[[0, 0], [1, 0], [2, 0], [3, 0]]])
                elif pixel == 60:
                    info.append([6,[[0, 1], [1, 1], [2, 0], [2, 1]]])
                elif pixel == 35:
                    info.append([7,[[0, 0], [0, 1], [1, 1], [2, 1]]])
                y2 = (y-12) // 24
                x2 = (x-12) // 24
                while True:
                    y2 -=1
                    if y2 < 0:
                        break
                    if board[y2][x2] == "0":
                        board[y2][x2] = "#"
                        break            
        board.append(row)
   
    return np.array(board)
def drop(poss,board):
    while True:
        for num in poss:
            if num[1] < 19:
                if board[num[1] + 1][num[0]] == "0":
                    break
            else:
                break
        else:
            for num in poss:
                num[1] += 1
            continue
        break
    return poss
    
def tryAll(board,poss,AllPossibles,moves,rotate,typ,types):
    possibles = []
    
    while poss[-1][0] <= 9:
        move = [rotate,poss[0][0]]
        temp = drop(deepcopy(poss),board)
        if not(temp in AllPossibles or temp in possibles):
            possibles.append(temp)
            types.append(typ)
            moves.append(move)
        for num in poss:
            num[0] += 1
    return possibles
def moveTopLeft(pos):
    pos = sorted(pos,key = lambda y : y[1])
    while pos[0][1] > 0 or pos[0][1] < 0:
        value = 0
        if pos[0][1] > 0:
            value = -1
        else:
            value = 1
        for num in pos:
            
            num[1] += value
    pos = sorted(pos,key = lambda x : x[0])
    while pos[0][0] > 0 or pos[0][0] < 0:
        value = 0
        if pos[0][0] > 0:
            value = -1
        else:
            value = 1
        for num in pos:
            num[0] += value
    



def move(board,coords,boards,moves,typ): 
    
    theMove = []
    for y in range(len(boards)):
        
        if (boards[y] == board).all():
            theMove = moves[y]
    
    for num in range(theMove[0]):
        keyboard.press("up arrow")
        keyboard.release("up arrow")
        #time.sleep(0.1)
    for x in range(9):
        keyboard.press("left arrow")
        keyboard.release("left arrow")
    
    absolute = theMove[1]
  
    while absolute != 0:
        keyboard.press("right arrow")
        keyboard.release("right arrow")
        #time.sleep(0.3)
        absolute -=1
    keyboard.press(" ")
    keyboard.release(" ")
   
    

def Grader(board,coordNew,moves,typ,types): #coords are kinda useful
    scores = []
    pointModif = [
        100000, #no holes
        150, #can score
        40, #max blocks covered
        10, #max blocks covered (self blocks)
        10000, #least distance from bottom
        


    ]
    

    #phase 1 : any air pockets that'll be made if placed here?
    
    for i in range(len(coordNew)):
        scores.append(0)
        currentBoard = board[i]
        good = True
        for e in range(len(coordNew[i])):
            the = coordNew[i][e]
            if (the[0]<19): #19 is floor
                if (currentBoard[the[0]+1][the[1]] == "#"):
                    good = False
                    break
        if (good):
            scores[i] += pointModif[0]
            

            

        
    #phase 2 of testing : can it score points? (normally you'd want to stack high for big points but screw that)
    
    for i in range(len(board)):
        currentBoard = board[i]
        for e in range(len(coordNew[i])):
            if (not "#" in currentBoard[coordNew[i][e][0]]):
                scores[i] += pointModif[1]


    #phase 3 of testing : how many blocks would be covered by them (maximize this!)      

    for i in range(len(coordNew)):
        currentBoard = board[i]
        covered = 0
        for e in range(len(coordNew[i])):
            the = coordNew[i][e]
            if (the[0]<19): #19 is floor
                deez = currentBoard[the[0]+1][the[1]]
                if (not deez == "#"):
                    if (deez == "N"):
                        scores[i] += pointModif[3]
                    else:
                        scores[i] += pointModif[2]
            else:
                scores[i] += pointModif[2]

                
    for i in range(len(coordNew)):
        for e in range(len(coordNew[i])):
            scores[i] += pointModif[4] * coordNew[i][e][0]
    topI = 0
    topScore = 0
    for i in range(len(scores)):
        if (scores[i]>topScore):
            topScore = scores[i]
            topI = i
    global held
    if types[topI] != typ:
       
        keyboard.press("c")
        keyboard.release("c")
        move(board[topI],coordNew[topI],board,moves,held[0])
        held[0] = held[2]
        held[1] = held[3]
        return
        
    move(board[topI],coordNew[topI],board,moves,typ) #i dont see a situation where it'll crash due to no placement being available
def DoTheSpin(board,pos,AllPossible,moves,typ,types):
    for rotate in range(4):
        AllPossible += tryAll(board,deepcopy(pos),AllPossible,moves,rotate,typ,types)
        if typ in [1,2,3,6,7]:
            offset = [1.5,1.5]
        elif typ == 5:
            offset = [2.5,1]
        elif typ == 4:
            break
        for num in pos:
            num[0] -= offset[0]
            num[1] -= offset[1]
            temp = num[0]
            num[0] = math.floor(-1 * num[1] + offset[0])
            num[1] =  temp
            num[1] = math.floor(offset[1] + num[1])
        pos = sorted(pos,key = lambda x : x[0])
        moveTopLeft(pos)
        pos = sorted(pos,key = lambda x : x[0])
    
def yes():
    info = []
    board = GetState(info)
    pos = []
    for y in range( len(board) - 1):
        for x in range( len(board[y]) - 1):
            if board[y][x] == "C":
                pos.append([x,y])
    pos = info[0][1]
    
    type = info[0][0]#1 green z, 2 red z,3 T,4 square,5 line,6 orange L,7 blue L
    global held
    if held[0] == "null":
        held[0] = type
        held.append(pos)
        held.append(type)
        held.append(pos)
        keyboard.press("c")
        keyboard.release("c")
        return
    held[2] = type
    held[3] = pos
    AllPossible = []
    moves = []
    types = []
    DoTheSpin(board,pos,AllPossible,moves,type,types)
    DoTheSpin(board,held[1],AllPossible,moves,held[0],types)
    
    allBoards = []
    allNewCoords = []
    for y in board:
        for x in y:
            if x == "C":
                x = "#"
    for possible in AllPossible:
        tempB = deepcopy(board)
        yes = []
        for nums in possible:
            tempB[nums[1]][nums[0]] = "N"
            yes.append([nums[1],nums[0]])
        allBoards.append(tempB)
        allNewCoords.append(yes)
   
    Grader(allBoards,allNewCoords,moves,type,types)
def main():
    time.sleep(1)
    print("go")
    while True:
        yes()
        #time.sleep(0.2) #comment for SPEEE
        

noClick = """ #uncomment if no like
def L(): #ey yo sorry for doing this but yes
    global clicks #this is a bad idea
    global bboxthing
    print(clicks)
    
    if (clicks==1):
        lol = mouse.get_position()
        bboxthing = [lol[0],lol[1],lol[0]+240,lol[1]+480]
        print(bboxthing)
    elif(clicks==0):
        main()
        print("done")
    clicks = clicks - 1

mouse.on_click(lambda : L())
""" #uncomment this aswell
    
main() #i do click so uh yes uncomment if you want
#print("done")
