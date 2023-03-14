data = open("WordSearch.txt","r").read().split("---")
words = data[1].split("\n")
board = []
for y in data[0].split("\n"):
    row = []
    for x in y.split(" "):
        row.append(x)
    board.append(row)
board.pop()
def search_in_direction(x,y,direction,word,index,solution,board):
    if index == len(word):
        return True
    if board[y][x] == word[index]:
        solution.append([x,y])
        if search_in_direction(x+direction[0],y+direction[1],direction,word,index+1,solution,board):
            return True
        else:
            return False
    else:
        return False
def search_Around(x,y,word,board,solution):
    directions = []
    if x > 0:
        if board[y][x-1] == word[1]:
            directions.append([-1,0])
        if y > 0:
            if board[y-1][x-1] == word[1]:
                directions.append([-1,-1])
        if y < len(board) - 1:
           
            if board[y + 1][x - 1] == word[1]:
                directions.append([-1,1])
    if x < len(board[0]) - 1:
        if board[y][x+1] == word[1]:
            directions.append([1,0])
        if y > 0:
            if board[y-1][x+1] == word[1]:
                directions.append([1,-1])
        if y < len(board)-1:
            if board[y+1][x+1] == word[1]:
                directions.append([1,1])
    if y > 0:
        if board[y-1][x] == word[1]:
            directions.append([0,-1])
    if y < len(board)-1:
        if board[y+1][x] == word[1]:
            directions.append([0,1])
    for d in directions:
        solution.append([x,y])
        if search_in_direction(x + d[0],y + d[1],d,word,1,solution,board):
            return solution
        else:
            solution.clear()
    
def Search(word,board):
    solution = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == word[0]:
                if search_Around(x,y,word,board,solution):
                    return solution
                
answer = Search("TEST",board)
print(list(map(lambda x : [x[0]+1,x[1]+1],answer)))
words = [board[x[1]][x[0]] for x in answer]
