# Far more consise than part 1. The problem with the code in part 1
# thus must have been the function string_memory_count I guess

def string_code_count(string: str) -> int:
    return len(string) - 1

def string_encoded_count(string: str) -> int:
    return 2 + string_code_count(string) + len([c for c in string if (c == "\\" or c == "\"")])

with open("2015/Day 8/input.txt") as f:
    filecontents = f.readlines()

    code_char_count = 0
    encoded_count = 0

    for string in filecontents:
        code_char_count += string_code_count(string)
        encoded_count += string_encoded_count(string)

    difference = encoded_count - code_char_count
    print(f"The difference between code and memory is {difference}")