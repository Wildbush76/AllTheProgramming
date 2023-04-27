def decode(data, current, to):
    yea = [chr(int(x, current)) for x in data.strip().split(" ")]
    yea = "".join([str(i) for i in yea])
    current += 1
    if current > to:
        return yea
    else:
        print(f"base {current}")
        return decode(yea, current, to)


count = int(input("count to what "))
file = open("Encoded.txt", "r")
data = file.read()
print(decode(data, 2, count))
file.close()
