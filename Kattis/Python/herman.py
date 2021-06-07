# https://open.kattis.com/problems/herman
import math


def solve(r):
    print("%.6f" % (math.pi * r**2))
    print("%.6f" % (2 * r**2))


solve(int(raw_input()))
