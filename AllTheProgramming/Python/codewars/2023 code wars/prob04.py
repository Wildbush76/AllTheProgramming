data = ""
find = ""
with open("prob04-1-in.txt") as file:
    find = file.readline().strip()
    data = file.readline().strip()

index = data.find(find)
print(f"{find} is at index: {index}")