from math import *

# Att appenda alla divisors i lista och räkna len(divisors) är långsammare
# än counter.


def check(n):
    divisors = [n]
    x = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            x += 1
            if x > 499:
                return True


x = 0
divisors = []
c = 0


for i in range(1, 1000000):
    x += i
    check(x)
    c += 1
    if check(x):
        print(x, c)
        break

input()
