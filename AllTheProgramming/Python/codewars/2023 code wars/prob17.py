with open("prob17-2-in.txt") as file:
    thing = file.read().strip()
    for i in range(1,len(thing),1):
        fun = [thing[e:e+i]for e in range(0,len(thing),i)]
        for e in range(1,len(fun)-1):
            if not fun[0]==fun[e]:
                break
        else:
            
            print(fun[0][(len(fun[-1])):])
            print(fun[0])
            break