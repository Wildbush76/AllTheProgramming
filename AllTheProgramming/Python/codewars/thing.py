data = open("UniBaker.txt","r").read().split("\n")
size = int(data[0])
data = data[1:]
import time
class cupCake:
    def __init__(self,value,pos):
        self.value = value
        self.orginal = value
        self.pos = pos
def PrintBoard(board):
    for i in board:
            print("".join(list(map(lambda x : x.value,i))))
def MakeBoard(data,size):
    board = []
    unknown = []
    for y in range(size):
        row = []
        for x in range(size):
            row.append(cupCake(data[y][x],[y,x]))
            if data[y][x] == "?":
                unknown.append(row[-1])
        board.append(row)
    return board, unknown
def CheckValid(board,size):
    #check for ring
    letters = "".join(list(map(lambda x : x.value,board[0] + board[-1])))
    letters += "".join(list(map(lambda x : x[0].value,board)))
    letters += "".join(list(map(lambda x : x[-1].value,board)))
    if ("." in letters) ^ ("#" in letters):
        return False
    #check for 2x2 
    for y in range(0,size-1,2):
        for x in range(0,size-1,2):
            area = [board[y][x].value,board[y][x+1].value,board[y+1][x].value,board[y+1][x+1].value ]

            if area.count(area[0]) == 4 and area[0] != "?":
                return False
    TotalWhite = 0
    TotalBrown = 0
    for y in range(size):
        for x in range(size):
            V = board[y][x].value
            if V == "?":
                continue
            elif V == ".":
                TotalWhite+=1
            else:
                TotalBrown+=1
            if x > 0:
               if V == board[y][x-1].value or board[y][x-1].value == "?":
                    continue
            if x < size-1:
                if V == board[y][x+1].value or board[y][x+1].value == "?":
                    continue
            if y > 0:
                if V == board[y-1][x].value or board[y-1][x].value == "?":
                    continue
            if y < size-1:
                if V == board[y+1][x].value or board[y+1][x].value == "?":
                    continue
            return False
    def Search(cord,countedCords,size):
        Value = board[cord[0]][cord[1]].value
        f = False
        
        if cord[1] < size-1:
            if Value == board[cord[0]][cord[1]+1].value and not([cord[0],cord[1]+1] in countedCords):
                if cord not in countedCords:
                    countedCords.append(cord)
                Search([cord[0],cord[1]+1],countedCords,size)
                f = True
        if cord[1] > 0:
            if Value == board[cord[0]][cord[1]-1].value and not([cord[0],cord[1]-1] in countedCords):
                if cord not in countedCords:
                    countedCords.append(cord)
                Search([cord[0],cord[1]-1],countedCords,size)
                f = True
        if cord[0] > 0:
            if Value == board[cord[0]-1][cord[1]].value and not([cord[0]-1,cord[1]] in countedCords):
                if cord not in countedCords:
                    countedCords.append(cord)
                Search([cord[0]-1,cord[1]],countedCords,size)
                f = True
        if cord[0] < size-1:
            if Value == board[cord[0]+1][cord[1]].value and not([cord[0]+1,cord[1]] in countedCords):
                if cord not in countedCords:
                    countedCords.append(cord)
                Search([cord[0]+1,cord[1]],countedCords,size)
                f = True
        if not f and not(cord in countedCords):
             countedCords.append(cord)
       

        
    CountedWhiteCords = []
    CountedBrownCords = []
    WB = [False,False]
    for y in range(size):
        for x in range(size):
            if WB[0] and WB[1]:
                break
            V = board[y][x].value
            if V == ".":
                if WB[0]:
                    continue
                Search([y,x],CountedWhiteCords,size)
                if len(CountedWhiteCords) != TotalWhite:
                    return False
                WB[0] = True
                
            else:
                Search([y,x],CountedBrownCords,size)
                if len(CountedBrownCords) != TotalBrown:
                    return False
                WB[1] = True
        else:
            continue
        break
    return True

board, unknowns = MakeBoard(data,size)
#number = ("1" * len(unknowns))
#number = list(map(lambda x : int(x),number))
for x in unknowns:
    x.value = "."
print("Go")
current = 0
while True:
    if current == len(unknowns):
        for i in board:
            print("".join(list(map(lambda x : x.value,i))))
        break
    for val in [".","#","?"]:
        unknowns[current] = val
        if CheckValid(board,size):
            current += 1
            break
    else:
        if current > 0:
            current -= 1
        else:
            print("yea that is not right")
            raise Exception("something went wrong you idoit")
    '''
    if CheckValid(board,size):
        print("done!")
        for i in board:
            print("".join(list(map(lambda x : x.value,i))))
        break
    else:
        number[0]+=1
       
        for i in range(len(number)):
            if number[i] == 3:
                number[i] = 1
                if i == len(number)-1:
                    print("oh no")
                else:
                    number[i + 1] += 1
        for num in range(len(unknowns) - 1):
            if number[num] == 1:
                unknowns[num].value = "."
            elif number[num] == 2:
                unknowns[num].value = "#
                '''
                
    
