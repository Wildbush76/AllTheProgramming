data = open('C:\\Users\\wildb\\OneDrive\\Desktop\\2023 code wars\\prob02-1-in.txt')
while True:
    line = data.readline().strip()
    if int(line) == 0:
        break
    elif int(line)%4==0:
        print(line + '/4 = ' + str(int(line)//4))