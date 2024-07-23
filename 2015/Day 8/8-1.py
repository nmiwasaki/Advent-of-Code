# //
# /"
# /xhh

def string_code_count(string: str) -> int:
    return len(string) - 1

def string_memory_count(string: str) -> int:
    count = 0
    i = 0
    while i < len(string):
        if string[i] == "\\" and string[i + 1] == "x":
            count += 1
            i += 4
        elif string[i] == "\\":
            count += 1
            i += 2
        elif string[i] == "\n":
            break
        else:
            count += 1
            i += 1
    return count - 2        # for ""

with open("2015/Day 8/input.txt") as f:
    filecontents = f.readlines()

    code_char_count = 0
    memory_char_count = 0

    for string in filecontents:
        code_char_count += string_code_count(string)
        memory_char_count += string_memory_count(string)

    difference = code_char_count - memory_char_count + 1
    # I'm short somewhere but I have no clue why

    print(f"The difference between code and memory is {difference}")
    