with open("prob13-2-in.txt") as file:
    TheInfo = file.read().split("\n")[:-2]
    #print(TheInfo)
    for i in range(len(TheInfo)):
        TheInfo[i] = TheInfo[i].split("-")
        for e in range(len(TheInfo[i])-1):
            TheInfo[i][e] = "x" * len(TheInfo[i][e])
            print(TheInfo[i][e],end="")
            if (e<len(TheInfo[i])-2):
                print("-",end="")
            else:
                print("-"+TheInfo[i][e+1])