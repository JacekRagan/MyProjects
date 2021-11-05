from random import randint
file = open("psc.txt", "w")
a = 0
b = 0
for i in range(1000000):
    if b%15 == 0:
        print("0", file=file)
    print(randint(1,9), file=file)
    b = b + 1
    if b % 15 == 0:
        print("",file=file)




