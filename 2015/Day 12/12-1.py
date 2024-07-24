# Solution that has nothing to do with part 2
import re

f = open("2015/Day 12/input.txt")
filecontents = f.read()
f.close()

pattern = r"(-?\d+)"
numbers = re.findall(pattern, filecontents)

total = sum([int(num) for num in numbers])
print(f"The total is {total}")