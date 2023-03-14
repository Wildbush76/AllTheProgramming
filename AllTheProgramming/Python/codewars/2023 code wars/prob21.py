import math

with open("C:/Users/wildb/OneDrive/Desktop/AllTheProgramming/Python/codewars/2023 code wars/codewars/student_datasets/prob21-1-in.txt") as file:
    totalDistance = float(file.readline().strip()) * 1000

    people = [file.readline().strip().split(" ")]
    while people[-1] != ["00"]:
        people.append(file.readline().strip().split(" "))
    people = people[:-1]

peopleV2 = []


for person in people:
    totalTime = 0
    totalDistance = 0
    p = person[1].split(";")
    for i in p:
        i = i.split(":")

        timez = list(map(int, i[0].split("-")))
        time = timez[1] - timez[0]
        totalTime += time
        totalDistance += time * float(i[1])
    totalTime = math.trunc(totalTime/60 * 10)/10
    peopleV2.append([person[0], totalDistance, totalTime])

toBeSorted = [[x, index] for index, x in enumerate(peopleV2)]
toBeSorted = sorted(toBeSorted, key=lambda x: x[0][1], reverse=True)

place = 1

output = []

for i in toBeSorted:
    o = f"%s %.2fm in %fmin (%d" % (i[0][0], i[0][1], i[0][1], place)
    if place == 1:
        o += "st"
    elif place == 2:
        o += "nd"
    elif place == 3:
        o += "rd"
    else:
        o += "th"
    o += ")"
    output.append([o, i[1]])
    place += 1
output = sorted(output, key=lambda x: x[1])

for ee in output:
    print(ee[0])
