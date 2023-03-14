from functools import reduce



def comedy(x,y):
    print(f"{x} + {y} = {x+y}")
    return x + y

with open("prob20-3-in.txt") as file:
    num = int(file.readline().strip())
power = 512
bits = []
powers = []
while power>=1:
    if num>=power:
        num -= power
        print(str(power) + '=1')
        bits.append(1)
        powers.append(power)
    else:
        print(str(power) + '=0')
        bits.append(0)
    power //= 2
statements = []
power = 512
num2 = 0

funni = reduce(comedy,powers)
print(f"{funni} = ",end="")
found1 = False
bitString = ''
for bit in bits:
    if bit == 1:
        bitString += '1'
        found1 = True
    elif bit == 0 and found1:
        bitString += '0'
print(bitString)
