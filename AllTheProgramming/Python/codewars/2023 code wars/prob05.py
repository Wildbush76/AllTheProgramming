with open("prob05-1-in.txt") as file:
    string = file.read().strip()
    endString = ""
    for i in string:
        base10 = ord(i)
        bits = ''
        for j in range(3):
            bits += str(int(base10%6))
            base10 -= base10%6
            base10 /= 6
        endString += bits[::-1]
    print(endString)

