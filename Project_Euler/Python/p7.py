

## New prime Brutus forcus

from math import *
import time

primes = [2]

target = input("\nThis generates a list of primes. How many primes? ")

start = time.time()

def prime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n%i==0:
            return False
            break
    return True

count = 3

while len(primes)<target:
    if prime(count)==True:
        primes.append(count)
        count += 2
    else:
        count += 2

elapsed = (time.time() - start)

### Choices

print("\nList Generated in %s seconds." % (elapsed))

choice = input("\nDo you want to print the list?\n1 for Yes\n2 for No\n")
if choice == 1:
    print("\n")
    print(primes)
    choice = 3

if choice != 3:
    choice = input("\nDo you want to print a prime at certain index? \n1 for Yes\n2 for No\n")

if choice == 1:
    index = input("\nPlease enter index: ")
    print(primes[index])
