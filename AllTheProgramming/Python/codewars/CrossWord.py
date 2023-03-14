file = open("CrossWordData.txt")
data = file.read().split("\n-------\n")
class puzzle:
    def __init__(self,number,direction,length,cords):
        self.number = number
        self.direction = direction
        self.length = length
        self.letter = []
        self.pos = []
        for i in range(length):
            if direction == "H":
                self.pos.append([cords[0] + i,cords[1]])
            else:
                self.pos.append([cords[0],cords[1] + i])
            self.letter.append("#")
        
#get the puzzles
puzzles = []
for puz in data[0].split("\n"):
    info = puz.split(" ")
    puzzles.append(puzzle(int(info[0]),info[1],int(info[2]),[int(info[3]),int(info[4])]))
#add hints
for hint in data[1].split("\n"):
    info = hint.split(" ")
    for puzz in puzzles:
        for cord in puzz.pos:
            if cord == [int(info[0]),int(info[1])]:
                puzz.letter[puzz.pos.index(cord)] = info[2]
                
#add the words
used_words = []
words = data[2].split("\n")

for puzz in puzzles:
    for word in words:
        if len(word) != int(puzz.length):
            continue
        if word in used_words:
            continue
       
        for letter in range(len(word)-1):
            if puzz.letter[letter] != "#" and word[letter] != puzz.letter[letter]:
                break
        else:
            puzz.letter = word
            used_words.append(word)
            break
for puzz in puzzles:
    print(str(puzz.number).zfill(2) + " is " + "".join(puzz.letter))
