# Should be an incredibly easy conversion!

import re
from typing import List

def update_lights(lights: List[bool], instruction: str, x0: int, y0: int, x1: int, y1: int):
    operation = None
    if instruction == "turn on":
        operation = 1
    elif instruction == "turn off":
        operation = -1
    elif instruction == "toggle":
        operation = 2
    else:
        print("INSTRUCTION ERROR")
    
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            lights[i][j] += operation
            if lights[i][j] < 0:
                lights[i][j] = 0




with open("2015/Day 6/input.txt") as f:
    instructions = f.readlines()

    lights = list()
    for i in range(1000):
        column_vector = list()
        for j in range(1000):
            column_vector.append(0)
        lights.append(column_vector)

    pattern = r"([a-z ]+) (\d+),(\d+) through (\d+),(\d+)"
    for instruction in instructions:
        match = re.match(pattern, instruction)
        if match:
            update_lights(lights, match.groups()[0], int(match.groups()[1]), int(match.groups()[2]), int(match.groups()[3]), int(match.groups()[4]))
        else:
            print("REGEX CAPTURE ERROR")
            break

    luminance = 0
    for column in lights:
        for light in column:
            luminance += light
            
    print(f"The brightness of the enabled lights is {luminance}")