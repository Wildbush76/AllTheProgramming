import numpy as np

with open("input.txt","r") as file:
    data = [i.strip() for i in file.readlines()]

board = data[:-2]
movements = data[-1]

position = [0,0]
direction = [1,0]

for i in board:
    print(i)

#do everything loop
for step in movements:
    #do the thing
    if step in ["R","L"]:
        if step == "R":
            direction = [direction[1], -direction[0]]
        else:
            direction = [-direction[1], direction[0]]
    else:
        position = [x + y for x,y in zip(position,direction)]
        if abs(position[1]) > len(board)-1:
            position[1] = 0
            
        if abs(position[0]) > len(board[position[1]])-1:
            position[0] = 0
        

        if board[position[1]][position[0]] == "#":
            position = [x - y for x,y in zip(position,direction)]
print((abs(position[0])+1) * 1000 + (abs(position[1]) + 1)*4)
print(direction)