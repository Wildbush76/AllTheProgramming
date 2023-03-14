import os

PATH = ""


def searchDir(dir: str, whatWeFinding: str, checkForIt: bool) -> str:
    for item in os.listdir():
        coolerPath = os.path.join(dir, item)
        if os.path.isdir(coolerPath):
            if whatWeFinding in coolerPath:
                searchDir(coolerPath, whatWeFinding, True)
            else:
                searchDir(coolerPath, whatWeFinding, False)
        elif os.path.isfile(coolerPath) and checkForIt:
            print("we found it " + coolerPath)


with open("") as file:
    PATH = file.readline().strip()

    current = file.readline().strip()

    while current != "END":
        searchDir(PATH, current, False)
        current = file.readline().strip()
