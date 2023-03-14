num = 0
with open("prob11-3-in.txt") as file:
    num = int(file.readline().strip())

full = num//4
partial = num%4

output = ""

if full == 1:
    output += f"{full} full car"
elif full > 1:
    output += f"{full} full cars"

if partial > 0:
    if len(output) > 0:
        output += ", "
    output += "1 partial car"
print(output)