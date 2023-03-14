with open("C:/Users/wildb/OneDrive/Desktop/AllTheProgramming/Python/codewars/2023 code wars/codewars/student_datasets/prob23-1-in.txt") as file:
    sentence = file.readline().strip()
    [file.readline() for x in range(3)]
    temp = [x.split(":") for x in file.readline().strip().split(";")]
    touchingLetters = dict()
    for i in temp:
        touchingLetters[i[0]] = i[1].split(",")
    words = []
    word = file.readline().strip()
    while word != "ZZZZZ":
        words.append(word)
        word = file.readline().strip()

end = ""

for word in sentence.split(" "):
    off = []
    for testingWord in words:
        if len(word) != len(testingWord):
            continue
        numOff = 0
        for letters1, letters2 in zip(testingWord, word):
            if letters1 != letters2:
                numOff += 1
        off.append([testingWord, numOff])
    off = list(sorted(off, key=lambda x: x[1]))
    if len(off) == 1 or off[0][1] < off[1][1]:
        end += f"{off[0][0]} "
        continue
    for e in [x for x in off if x[1] == off[0][1]]:
        iDontKnowWhatImDoingAtThisPoint = [i for i in range(len(e)) if e[i] != word[i]]
        if e[iDontKnowWhatImDoingAtThisPoint[0]] in  touchingLetters[word[iDontKnowWhatImDoingAtThisPoint]]:
            end += f"{e} "

print(end)
