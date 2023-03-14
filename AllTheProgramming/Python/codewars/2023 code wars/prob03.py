import math
data = open('C:\\Users\\wildb\\OneDrive\\Desktop\\2023 code wars\\prob03-2-in.txt')
i = int(data.readline().strip())
maxPonies = int(data.readline().strip())
rate = float(data.readline().strip())
years = int(data.readline().strip())
ponies = math.trunc(i*(1+rate)*years)
print(f'At the current rate of growth there will be {ponies} ponies in {years} years')
if maxPonies-ponies<0:
    print(f'Celestia will need to add space for at least {ponies-maxPonies} ponies!')
else:
    print("Celestia won't need to add space yet!")