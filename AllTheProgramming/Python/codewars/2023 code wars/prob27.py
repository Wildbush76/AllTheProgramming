with open() as file:
    dail = int(file.readline().strip())
    dials = [0, 0, 0]

    sentences = []
    sent = file.readline().strip()
    while sent != ".":
        sentences.append(sent)
        sent = file.readline().strip()

for i in sentences:
    pass
