#Project Euler Problem 6

import time

start = time.time()

count=0
hyp=0

while count<100:
    count += 1
    hyp += count*count

count2=0
d=0

while count2<100:
    count2 += 1
    d += count2

f = d*d - hyp

elapsed = (time.time() - start)

print(f)
print(elapsed)
