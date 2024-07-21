def letters_pairs(word: str):
    # extract all two char substrings
    substrings = list()
    for i in range(0, len(word) - 1):
        substrings.append(word[i:i + 2])

    for i in range(0, len(substrings) - 2):
        for j in range(i + 2, len(substrings)):
            if substrings[i] == substrings[j]:
                return True
    return False

def sandwich(word):
    for i in range(2, len(word)):
        if word[i - 2] == word[i]:
            return True
    return False

def is_nice(word: str):
    return letters_pairs(word) and sandwich(word)

with open("2015/Day 5/input.txt") as f:
    filecontents = f.readlines()

    number_of_nice_strings = 0
    for string in filecontents:
        if is_nice(string):
            number_of_nice_strings += 1

    print(f"The number of nice strings is {number_of_nice_strings}")

