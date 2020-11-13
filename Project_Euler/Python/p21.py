
import time

start = time.time()

def div(n):
    divisors = [1]
    for i in range(2, int(n/2)+1):
        if n%i==0:
            divisors.append(i)
    return int(sum(divisors))


amicable = []

for i in range(2, 10000):
    x = int(div(i))
    z = int(div(x))
    if z==i and x!=i:
        amicable.append(i)

elapsed = (time.time() - start)


print("Result: %s found in %s seconds" % (sum(amicable), elapsed))
