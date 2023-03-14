with open("prob18-3-in.txt") as file:
    stuff = file.read().split("\n")[:-1]
word = stuff[0]

ing = stuff[1:]

output = ""


if(len(ing) < 2):
    print(f"{ing[0]}")
elif len(ing) < 3:
    print(f"{ing[0]} {word.lower()} {ing[1]}")
else:
    for index,i in enumerate(ing):
        if index == len(ing) - 1:
            output += word.lower() + " "
        output += i + ", "
    print(output[:-2])