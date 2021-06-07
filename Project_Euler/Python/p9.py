
from math import *

# Solution for problem 9
# Works fine, within reasonable time, simple solution, for some reason it won't,
# break at if, not sure why

x = 0
check = [0, 0, 0]

for i in range(1, 10000):
    for j in range(1, 10000):
        a = i**2
        b = j**2
        c = a + b
        d = sqrt(c)
        check[0] = i
        check[1] = j
        check[2] = d
        if sum(check) == 1000:
            print(check)
            break

print("Done!")
