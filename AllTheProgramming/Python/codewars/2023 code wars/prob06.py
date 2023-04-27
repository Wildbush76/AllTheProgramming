with open("prob06-2-in.txt") as file:
    while True:
        data = file.readline().strip().split(" ")
        if int(data[0]) == 0 and int(data[1]) == 0:
            break
        num = 0
        if data[2] == "D":
            num = int(data[0]) * 2 + 160 + int(data[1]) * 2 + 160
            print(f"Diagonal {num}")
        else:
            num = int(data[0]) * 2 + 40 + int(data[1]) * 2 + 40
            print(f"Square {num}")
