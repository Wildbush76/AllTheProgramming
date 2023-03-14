import math
with open("prob09-1-in.txt") as file:
    cars = int(file.readline().strip())
    time = int(file.readline())
    listCars = []
    for i in range(cars):
        listCars.append(file.readline().strip().split(" ",1))
    for i in listCars:
        distance = int(i[0])
        distance = (distance/60)*time
        trunct = math.trunc(distance*100)/100
        print(f"(%.2f)"%trunct,end="")
        while distance>=5:
            print("-",end="")
            distance -=5
        while distance>=1:
            print("~",end="")
            distance -=1
        while distance>=0.25:
            print("{}",end="")
            distance -=0.25
        print(i[1])
