import math


def createTrees(num: int, thestuff: set, prev: list):
    for i in range(1, math.ceil(num/2) + 1):
        if num % i == 0 and i != 1:
            i2 = num//i
            output = [i, i2] + prev
            output = map(str, sorted(output, reverse=True))
            thestuff.add(f"({'*'.join(output)})")
            createTrees(i, thestuff, prev.copy() + [i2])
            createTrees(i2, thestuff, prev.copy() + [i])


with open("C:/Users/wildb/OneDrive/Desktop/AllTheProgramming/Python/codewars/2023 code wars/codewars/student_datasets/prob26-1-in.txt") as file:
    data = int(file.readline().strip())
    while data != 0:
        output = set()
        createTrees(data, output, [])
        if output == set():
            data = int(file.readline().strip())
            continue
        output = sorted(output, key=lambda x: tuple(
            map(int, x.strip("()").split("*"))), reverse=True)
        print(f"{data} = " + ", ".join(output))
        data = int(file.readline().strip())
