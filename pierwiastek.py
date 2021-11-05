import math
import random
file = open("pierwiastek.txt", "w")
for i in range(10000000):
    a = random.randint(9999, 1000000)
    b = (math.sqrt(a))
    if b == int(b):
        print(a)
        print(b, file=file)
        print("udalo sie")
        print("")

    else:
        print(a)
        print(b)
        print("nie udalo sie")
        print("")

