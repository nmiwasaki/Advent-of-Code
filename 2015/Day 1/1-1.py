import os

# print("Current directory: ", os.getcwd())

with open('2015/Day 1/input.txt') as f:
    filecontents = f.read()
    floor = 0
    for i in filecontents:
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        else:
            print("ERROR")
            break
    print(f"The elevator stops at floor {floor}")