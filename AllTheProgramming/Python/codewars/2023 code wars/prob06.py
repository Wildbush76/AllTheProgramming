with open("prob06-2-in.txt") as file:
    while True:
        stupid = file.readline().strip().split(" ")
        if int(stupid[0]) == 0 and int(stupid[1]) == 0:
            break
        num = 0
        if stupid[2] == "D":
            num = int(stupid[0]) * 2 + 160 + int(stupid[1]) * 2 + 160
            print(f"Diagonal {num}")
        else:
            num = int(stupid[0]) * 2 + 40 + int(stupid[1]) * 2 + 40
            print(f"Square {num}")