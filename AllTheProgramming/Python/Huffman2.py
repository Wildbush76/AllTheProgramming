import json
text = open("text.txt","r").read()
tree = [["STOP",1]]
for letter in text:
    for item in tree:
        if item[0] == letter:
            item[1] += 1
            break
    else:
        tree.append([letter,1])
while len(tree) > 2:
    tree = sorted(tree,key = lambda x : x[-1])
    new = [tree[0][:-1],tree[1][:-1],tree[0][-1]+tree[1][-1]]
    tree = tree[2:]
    tree.append(new)
key = []
def CreateKey(search,key,code):
    if type(search[0]) == list:
        CreateKey(search[0],key,code+"0")
    else:
        for let in key:
            if search[0] == let[0]:
                break
        else:
            key.append((search[0],code))
    if len(search) > 1:
        if type(search[1]) == list:
            CreateKey(search[1],key,code+"1")
        else:
            for let in key:
                if search[1] == let[0]:
                    break
            else:
                key.append((search[1],code))
CreateKey(tree,key,"")
key = sorted(key,key = lambda x : len(x[1]))
encoded = ""
for letter in text:
    for find in key:
        if letter == find[0]:
            encoded += find[1]
for find in key:
    if find[0] == "STOP":
        encoded += find[1]
        stop = bytes(int(find[1],2))
        break
final = []
for i in range(0,len(encoded),8):
    final.append(int(encoded[i:i+8],2))
final = bytes(final)
with open("final","w") as file:
    file.write(json.dumps(tree))
with open("final2","ab") as file:
    file.write(final)
    
