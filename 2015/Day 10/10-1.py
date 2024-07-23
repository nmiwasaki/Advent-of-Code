# A solution not-at-all pythonic, but I don't mind very much

f = open("2015/Day 10/input.txt")
number = str(int(f.read()))
f.close()
print(number, type(number))

N = 40

for i in range(N):
    new_number = ""
    while number != "":
        i = 0           # index of string
        D = number[i]   # digit being looked for
        n = 1           # contiguous occurences of D
        while i < len(number) - 1:
            if number[i + 1] == D:
                n += 1
                i += 1
            else:
                break
        new_number += str(n) + str(D)
        number = number[i + 1:]
    number = new_number

print(f"After applying the process {N} times, the length of the result is {len(str(number))}")