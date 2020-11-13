

from math import *
import time

#Problem_10, tappat filen sa gor en ny

target = int(input("I want the sum of all primes below: "))

start = time.time()

primes = [2]

def prime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True

for i in range(3, target+1, 2):
    if prime(i)==True and i<target:
        primes.append(i)

elapsed = (time.time() - start)

print("Sum of all primes below %s is %s. Results found in %s seconds" % (target, sum(primes), elapsed))
