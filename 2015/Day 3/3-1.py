with open("2015/Day 3/input.txt") as f:
    radio = f.read()

    santa_x = 0     # positions
    santa_y = 0

    houses_visited = set()
    houses_visited.add((0,0))       # present is of course given to the first house @ O
    houses_with_multiple_presents = set()

    for dir in radio:
        if dir == ">":
            santa_x += 1
        elif dir == "^":
            santa_y += 1
        elif dir == "<":
            santa_x -= 1
        elif dir == "v":
            santa_y -= 1
        else:
            print("ERROR")
            break
        
        current_position = (santa_x, santa_y)
        if current_position in houses_visited:
            houses_with_multiple_presents.add(current_position)
        else:
            houses_visited.add(current_position)

    
    print(f"The total number of households with presents is is {len(houses_visited)}")
    print(f"The number of extra-lucky households this year is {len(houses_with_multiple_presents)}")