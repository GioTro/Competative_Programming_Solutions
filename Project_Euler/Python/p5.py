#Euler Problem 5

#skip 2, only tries even integers since the solution has to be even
#still a bruteforcing method you can construct the number from primes


import time

start = time.time()

def check(n):
    for i in range(1,21):
        if n%i==0:
            continue
        else:
            return False
    return True

x=2

while not check(x):
    x += 2

elapsed = ( time.time() - start )
print("Smallest number divisible by numbers 1-20 is %s, results found in %s" % (x, elapsed))
