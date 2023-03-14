with open("prob08-1-in.txt") as file:
    base = int(file.readline().strip())
    target = int(file.readline().strip())
    i=0
    while base**i<target:
        i+=1
    print(str(base)+"^"+str(i)+" = " + str(base**i))