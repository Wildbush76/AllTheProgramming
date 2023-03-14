def getInSequence(num):
    numbers = [0, 1, 1]
    while len(numbers) <= num:
        numbers.append(sum(numbers[-3:]))
    return numbers[num]


with open("C:/Users/wildb/OneDrive/Desktop/AllTheProgramming/Python/codewars/2023 code wars/codewars/student_datasets/prob14-1-in.txt") as file:
    data = file.readline().strip()
    while data != "0 0":
        data = data.split(" ")
        print(getInSequence(int(data[0])) - getInSequence(int(data[1])))
        data = file.readline().strip()
