with open("prob19-2-in.txt") as file:
    theWord = file.readline().strip()
    size = int(file.readline().strip())
length = len(theWord)
sizeTrue = (2*size) + 2*(size-2)
mult = sizeTrue//length+1
mod = length-(sizeTrue%length)
theWord = theWord * mult
theWord = theWord[:-mod]
theWord = list(theWord)
theStuff = ""

for i in range(size):
    theStuff += theWord.pop(0)
print(theStuff)
for i in range(size-2):
    print(theWord.pop(-1) + (' '*(size-2)) + theWord.pop(0))
theStuff = ''
for i in range(size):
    theStuff += theWord.pop(-1)
print(theStuff)
