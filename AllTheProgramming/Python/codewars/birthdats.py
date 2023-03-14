file = open("prob05-1-in.txt","r")
birthdays = [file.readline()[:5] for x in range(int(file.readline()))]
duped = []
for y in birthdays:
    if birthdays.count(y) > 1 and y not in duped:
        duped.append(y)
if len(duped) == 0:
    print("duplicates: None")
else:
    print(len(duped))
    print("duplicates: " + " ".join(duped))
