
def swap(string,key):
    newString = ""
    for i in string:
        if i.lower() == key[0].lower():
            if i.islower():
                newString += key[1].lower()
            else:
                newString += key[1].upper()
        elif i.lower() == key[1].lower():
            if i.islower():
                newString += key[0].lower()
            else:
                newString += key[0].upper()

        else:
            newString += i
    return newString

with open("prob16-2-in.txt") as file:
    swapped = file.readline().strip().split(" ")

    
    stuff = []
    x = file.readline().strip()
    while x != "END":
        stuff.append(x)
        x = file.readline().strip()

    stuff = [swap(x,swapped) for x in stuff]
    stuff = sorted(stuff)
    stuff = [swap(x,swapped) for x in stuff]
    print("\n".join(stuff))