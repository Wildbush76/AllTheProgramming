import os

PATH = "C:/Users/wildb/OneDrive/Desktop/AllTheProgramming/Python/codewars/2023 code wars/codewars/student_datasets/files"


def searchDir(dir: str, whatWeFinding: str, checkForIt: bool) -> str:
    for item in os.listdir(dir):
        coolerPath = os.path.join(dir, item)
        if os.path.isdir(coolerPath):
            if whatWeFinding in coolerPath:
                searchDir(coolerPath, whatWeFinding, True)
            else:
                searchDir(coolerPath, whatWeFinding, False)
        elif os.path.isfile(coolerPath) and checkForIt and "trailers" in coolerPath:
            print(f"{whatWeFinding} trailer found at {coolerPath}")
            return True


with open("C:/Users/wildb/OneDrive/Desktop/AllTheProgramming/Python/codewars/2023 code wars/codewars/student_datasets/prob25-1-in.txt") as file:
    # PATH += file.readline().strip()
    PATH = os.path.join(PATH, file.readline().strip())

    current = file.readline().strip()

    while current != "END":

        if searchDir(PATH, current, False) == None:
            print(f"{current} trailer missing")
        current = file.readline().strip()
