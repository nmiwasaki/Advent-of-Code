import hashlib
import re

#print(hashlib.md5(b"abcdef609043").hexdigest())

SECRET_KEY = b"yzbqklnj"
pattern = r"(0+)"

number = 0

while True:
    suffix_bytes = str(number).encode()
    hash_this = SECRET_KEY + suffix_bytes
    hash = hashlib.md5(hash_this).hexdigest()
    
    match = re.match(pattern, hash)
    if match:
        length = len(match.groups()[0])
        if length >= 5:
            print(f"The answer is {number}")
            break
        
    number += 1