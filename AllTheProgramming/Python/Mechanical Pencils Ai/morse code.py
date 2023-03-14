import sys
yes = sys.stdin
#yes = open("1.in","r")
for cases in range(int(yes.readline())):
    data = [yes.readline().strip() for x in range(26)]
    encode = {}
    decode = {}

    for e in data:
        encode[e[0]] = e[2:].strip()
        decode[e[2:].strip()] = e[0]
    decode = [[x,decode[x]] for x in decode]
    toBeIn = yes.readline().strip()
    encoded = ""
    for num, letter in enumerate(toBeIn):
        if letter == " ":
            encoded += " "*4
        elif num != len(toBeIn)-1:
            encoded += encode[letter] + " "*3
        else:
            encoded += encode[letter]

    toBeDe = yes.readline().strip()
   
    
    decode = list(reversed(sorted(decode, key = lambda x : len(x[0]))))
    decode = {x[0]:x[1] for x in decode}
    for letter in decode:
        toBeDe = toBeDe.replace(letter,decode[letter])
    #print(toBeIn)
    toBeDe = toBeDe.replace("       ","_").replace("   ","")
    toBeDe = toBeDe.replace("_"," ")
    toBeDe.strip()
    print(encoded)
    print(toBeDe)
