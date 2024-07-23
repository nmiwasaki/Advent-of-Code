# Just modify N to 50
# Also, "just" wait 30 seconds. This script is incredibly slow.
import time

start = time.time()

f = open("2015/Day 10/input.txt")
number = str(int(f.read()))
f.close()

N = 50                  # Changed

for i in range(N):
    print(f"Iteration {i + 1}")
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

stop = time.time()

print(f"After applying the process {N} times, the length of the result is {len(str(number))}\nThis calculation required a time of {stop - start}")