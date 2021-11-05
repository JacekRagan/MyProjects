import math
import random
file = open("pierwiastek.txt", "w")
for i in range(1000):
    a = random.randint(1000, 1000000)
    b = (math.sqrt(a))
    if b == int(b):
        print(a, file=file)
        print(b, file=file)
        print("udalo sie")
        print("", file=file)

    else:
        print(a)
        print(b)
        print("nie udalo sie")
        print("")

