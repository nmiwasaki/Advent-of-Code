import hashlib
import re
import time

#print(hashlib.md5(b"abcdef609043").hexdigest())

NUMBER_OF_LEADING_ZEROES = 6
SECRET_KEY = b"yzbqklnj"
pattern = r"(0+)"

number = 0

start_time = time.time()

while True:
    suffix_bytes = str(number).encode()
    hash_this = SECRET_KEY + suffix_bytes
    hash = hashlib.md5(hash_this).hexdigest()
    
    match = re.match(pattern, hash)
    if match:
        length = len(match.groups()[0])
        if length >= NUMBER_OF_LEADING_ZEROES:
            print(f"The answer is {number}")
            break
        
    number += 1

end_time = time.time()

print(f"Elapsed time: {end_time - start_time}")