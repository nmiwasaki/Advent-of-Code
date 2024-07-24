f = open("2015/Day 11/input2.txt")
password = f.read()
f.close()

password = list(password)

def increment(password):
    done = False
    i = len(password) - 1
    while not done:
        if i < 0:
            raise OverflowError
        elif password[i] == "z":
            password[i] = "a"
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            done = True

def increasing(password):
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i]) + 2 == ord(password[i + 2]):
            return True
    return False

def not_contain(password):
    for c in password:
        if c == "i" or c == "o" or c == "l":
            return False
    return True

def doubles(password):
    pairs = 0   # Quantity
    i = 0
    while i < len(password) - 1 and pairs < 2:
        if password[i] == password[i + 1]:
            # pair found
            pairs += 1
            i +=2
        else:
            i += 1
    if pairs >= 2:
        return True
    else:
        return False
    
increment(password)     # The previous one expired

# Main
while True:
    if increasing(password) and not_contain(password) and doubles(password):
        printthis = "".join(password)
        print(f"The perfect password is {printthis}")
        break
    else:
        increment(password)