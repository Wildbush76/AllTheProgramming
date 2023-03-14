with open("C:/Users/wildb/OneDrive/Desktop/AllTheProgramming/Python/codewars/2023 code wars/codewars/student_datasets/prob28-1-in.txt") as file:
    grid = [list(file.readline().strip())
            for x in range(int(file.readline().strip()))]
print(grid)
