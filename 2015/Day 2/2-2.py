import re
import math

pattern = r"(\d+)x(\d+)x(\d+)"

with open("2015/Day 2/input.txt") as f:
    filecontents = f.readlines()

    ribbon_needed: int = 0

    for line in filecontents:
        match = re.match(pattern, line)
        if match:
            dimensions = [int(length) for length in match.groups()]
            ribbon_length = 2 * (sum(dimensions) - max(dimensions)) + math.prod(dimensions)
            ribbon_needed += ribbon_length

        else:
            print("ERROR")
            break
    print(f"The required length of ribbon is {ribbon_needed}")