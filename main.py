import time

start = time.clock()
count = 0
for i in range(100000000000):
    count += 1

end = time.clock()
print(end - start)
