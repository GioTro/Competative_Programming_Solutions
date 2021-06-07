# Problem https://open.kattis.com/problems/estimatingtheareaofacircle
import math

while(True):
    p, q, r = map(float, raw_input().split())
    if (p == 0 and q == 0 and r == 0):
        break
    print("{} {}".format(math.pi * p**2, (r * (2 * p)**2) / q))
