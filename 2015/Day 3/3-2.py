with open("2015/Day 3/input.txt") as f:
    radio = f.read()

    santa_pos = [0, 0]
    robo_pos = [0, 0]

    santas_turn = True # Santa always begins

    houses_visited = set()
    houses_visited.add((0,0))       # present is of course given to the first house @ O

    for dir in radio:
        if santas_turn:
            sleigh_pos = santa_pos      # this "pass an implicit pointer" thing has finally worked in my favour!!
        else:
            sleigh_pos = robo_pos

        if dir == ">":
            sleigh_pos[0] += 1
        elif dir == "^":
            sleigh_pos[1] += 1
        elif dir == "<":
            sleigh_pos[0] -= 1
        elif dir == "v":
            sleigh_pos[1] -= 1
        else:
            print("ERROR")
            break
        
        current_position = (sleigh_pos[0], sleigh_pos[1])
        houses_visited.add(current_position)

        santas_turn = not santas_turn # change who's moving

    
    print(f"The total number of households with presents is is {len(houses_visited)}")