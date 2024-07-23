"""
By far the most impressive thing I've done with regex so far
By far the saddest solution so far. The line of code:
lights[i][j] = operation(lights[i][j])
is pretty pathetic. I had orignally mistakenly written
operation(lights[i][j])
instead, but as it turns out Python doesn't support
pass by reference in ANY fashion. SAD!

Also the program is really slow. If there was a better
representation for the light grid rather than a list of lists
then it'd be far faster.
"""

import re
from typing import List

"""
Example inputs:
toggle 584,730 through 750,761
turn off 899,516 through 900,925
turn on 105,229 through 822,846
"""

def turn_on(light: bool):
    return True

def turn_off(light: bool):
    return False

def toggle(light: bool):
    return not light

def update_lights(lights: List[bool], instruction: str, x0: int, y0: int, x1: int, y1: int):
    operation = None
    if instruction == "turn on":
        operation = turn_on
    elif instruction == "turn off":
        operation = turn_off
    elif instruction == "toggle":
        operation = toggle
    else:
        print("INSTRUCTION ERROR")
    
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            lights[i][j] = operation(lights[i][j])

with open("2015/Day 6/input.txt") as f:
    instructions = f.readlines()

    lights = list()
    for i in range(1000):
        column_vector = list()
        for j in range(1000):
            column_vector.append(False)
        lights.append(column_vector)
    # The lights all start turned off.

    pattern = r"([a-z ]+) (\d+),(\d+) through (\d+),(\d+)"
    for instruction in instructions:
        match = re.match(pattern, instruction)
        if match:
            update_lights(lights, match.groups()[0], int(match.groups()[1]), int(match.groups()[2]), int(match.groups()[3]), int(match.groups()[4]))
        else:
            print("REGEX CAPTURE ERROR")
            break

    lights_enabled = 0
    for column in lights:
        for light in column:
            if light == True:
                lights_enabled += 1
    print(f"The number of enabled lights is {lights_enabled}")