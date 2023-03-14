def encode(input,offset):
    output = ""
    for letter in list(input.lower()):
        if(letter == " "):
            output += " "
            continue
        output += chr(((ord(letter.lower())-65) + offset)%26 + 65)
    return output

def decode(input):
    goodnesssValues = [0.0817,0.0149,0.0278,0.0425,0.1270,0.0223,0.0223,0.0609,0.0697,0.0015,0.0077,0.0402,.0241,0.0675,0.0751,0.0193,0.0009,0.0599,0.0633,0.0906,0.0276,0.0098,0.0236,0.0015,0.0197,0.0007]
    def getGoodness(input):
        num = 0
        for letter in list(input):
            if(letter == " "):
                continue 
            num += goodnesssValues[( ord(letter)-65)]
        return num
    possible = []#all possible offsets
    letters = list(input)
    for offSet in range(25):
        output = ""
        for letter in letters:
            if(letter == " "):
                output += " "
                continue
            num = ((ord(letter.lower())-65) + offSet)%26
            output += chr(num + 65)
        possible.append(output)
    poss = []
    for i in possible:
        poss.append((i,getGoodness(i)))
    poss.sort(key = lambda x:x[1])
    return poss[-1][0]
#print(deCode(input()))#decoder test
#print(enCode(input(),5))#incoder test
