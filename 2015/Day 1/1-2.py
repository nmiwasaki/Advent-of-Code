with open('2015/Day 1/input.txt') as f:
    filecontents = f.read()
    position = 0
    floor = 0
    for i in filecontents:
        position += 1
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        else:
            print("ERROR")
            break
        
        if floor == -1:
            print(f"The basement is reached at position {position}")
            break
