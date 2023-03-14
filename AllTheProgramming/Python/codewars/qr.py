data = open("prob19_4.in","r").read().replace("##","#").replace("  "," ")
layers = data.split("\n")#[:33]
layers.pop()
size = len(layers)-1
for y in range(8):
    if y == 6:
        layers[y] = "?" * 33
    else:
        layers[y] = ("?" * 8) + layers[y][8:25] + ("?" * 8)
    layers[y + 25] = ("?" * 8) + layers[y+25][8:]
for y in range(5):
    layers[y + 24] = layers[y + 24][:24] + "?" *5 + layers[y + 24][29:]
for y in range(33):
    layers[y] = layers[y][:6] + "?" + layers[y][7:]
#read it
output = ""
readUp = True
pos = [size,size]
while pos[0] > 0 or pos[1] > 0:
    output += layers[pos[0]][pos[1]]
    if readUp:
        pos[0] -= 1
    else:
        pos[0] += 1
    if pos[0] < 0 or pos[0] > size:
        pos[1] -= 1
        readUp = not readUp
        if pos[0] < 0:
            pos[0] += 1
        else:
            pos[0] -= 1

output = output.replace("?","").replace("#","1").replace(" ","0")
yes = []
for x in range(0,len(output),8):
    #test = output[x:x+8]
    #test= int(test,2)
    #yes.append(chr(int(test)))
    yes.append(int(output[x:x+8],2))
e =  bytes(yes)
print(e.decode("ascii"))
