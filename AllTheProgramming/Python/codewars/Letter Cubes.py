data = open("letterCubes.txt","r").read().split("\n")
numCubes = int(data[0])
Cubes = data[1:numCubes+1]
Cubes = list(map(lambda x:x.split(" "),Cubes))
Words = data[numCubes+2:]
WordNums = []
WordNums = []
def Main(NUMS):
    for x in NUMS:
        for y in x:
            if len(y) == 0:
                return False
    def yes(word):
        for letter in word:
            if len(letter) == 0:
                word.remove(letter)
        
    
for yes in Words:
    row = []
    for letter in yes:
        row.append([Cubes.index(x) for x in Cubes if letter in x])
    WordNums.append(row)
print(WordNums)

    
        
    
            
