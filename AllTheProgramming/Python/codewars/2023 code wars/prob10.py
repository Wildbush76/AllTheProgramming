import math

with open("prob10-4-in.txt") as file:
    birthday = file.readline().strip().split("-")
    currentDay = file.readline().strip().split("-")
    name = file.readline().strip()

monthCount1 = int(birthday[0]) * 12 + int(birthday[1]) + int(birthday[2])/30
mountCount2 = int(currentDay[0])*12 + int(currentDay[1]) + int(currentDay[2])/30

diff = math.trunc(mountCount2 - monthCount1)

print(f"{name} is {diff} months old")