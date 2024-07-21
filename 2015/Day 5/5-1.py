def vowel_count(word: str):
    count = 0
    for c in word:
        for v in ("a", "e", "i", "o", "u"):
            if c == v:
                count += 1
                break
    return count

def double_letter(word: str):
    for c in range (1, len(word)):
        if word[c] == word [c - 1]:
            return True
    return False

def forbidden_strings(word: str):
    for c in range(1, len(word)):
        if word[c - 1] == "a" and word[c] == "b":
            return True
        elif word[c - 1] == "c" and word[c] == "d":
            return True
        elif word[c - 1] == "p" and word[c] == "q":
            return True
        elif word[c - 1] == "x" and word[c] == "y":
            return True
    return False

def is_nice(word: str):
    return vowel_count(word) >= 3 and double_letter(word) and not forbidden_strings(word)







with open("2015/Day 5/input.txt") as f:
    filecontents = f.readlines()

    number_of_nice_strings = 0
    for string in filecontents:
        if is_nice(string):
            number_of_nice_strings += 1

    
    print(f"The number of nice strings is {number_of_nice_strings}")