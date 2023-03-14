with open("prob07-2-in.txt") as file:
    fizzer = []
    read = int(file.readline().strip())
    while (not read == 0):
        fizzer.append(read)
        read = int(file.readline().strip())
    for i in fizzer:
        fizzed = False
        if (i%5==0 or i%9==0):
            print(str(i) + " ",end="")
            if (i%5==0):
                print("FIZZ",end="")
                fizzed = True
            if (i%9==0):
                if (fizzed):
                     print(" FUZZ!",end="")
                else:
                    print("FUZZ",end="")
            print("")
            
