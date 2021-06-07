# Largest Palindrome Number
# Probleeemo 4

import time

start = time.time()


def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True


max = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if palindrome(i * j) and i * j > max:
            max = i * j

elapsed = (time.time() - start)

print(
    "\nThe largest palindrome number made from the product\nof two 2-digit numbers is %s. \nResults found in %s seconds\n" %
     (max, elapsed))
