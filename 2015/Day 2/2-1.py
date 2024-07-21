import re
pattern = r"(\d+)x(\d+)x(\d+)"

with open("2015/Day 2/input.txt") as f:
    filecontents = f.readlines()

    paper_needed: int = 0

    for line in filecontents:
        match = re.match(pattern, line)
        if match:
            dimensions = [int(length) for length in match.groups()]
            paper_size = 2 * (dimensions[0] * dimensions[1] + dimensions[1] * dimensions[2] + dimensions[2] * dimensions[0]) + \
                         min(dimensions[0] * dimensions[1], dimensions[1] * dimensions[2], dimensions[2] * dimensions[0])
            paper_needed += paper_size
        else:
            print("ERROR")
            break
    print(f"The required area of paper is {paper_needed}")