import os
import random
for i in range(10000):
    password_len = 5
    cos = ['A','W','Y', 'P', 'T', 'Q', 'X']
    POLSKA = ['a' ,'w', 't' ,'p']
    COMBINED_LIST = cos + POLSKA
    password = "".join(random.sample(COMBINED_LIST, password_len))
    print(password)
    os.mkdir(password)

