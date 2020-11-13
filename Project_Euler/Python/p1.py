
import time

a = 0
z = 0

target = input("Sum all multiples 3 and 5 below: ")

start = time.time()

while a<target-1:
    a += 1
    if a % 3 == 0 or a % 5 == 0:
        z += a

elapsed = (time.time() - start)

print("Implementation 1 found %s in %s seconds " % (z, elapsed))


print("\n")



###New implementantion below
start = time.time()

result = int(sum(list(i for i in range(1, target) if i%3==0 or i%5==0)))

elapsed = (time.time() - start)

print("Implementation 2 found %s in %s seconds " % (result, elapsed))
