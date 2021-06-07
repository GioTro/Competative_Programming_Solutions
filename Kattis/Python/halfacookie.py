import math
import sys


def length(c):
    return math.sqrt((c[0]**2 + c[1]**2))


def solve(c, r):
    if (length(c) > r):
        print("miss")
    else:
        theta = 2 * math.acos(length(c) / r)
        area1 = math.pi * (r**2)
        area2 = ((r**2)) * (theta - math.sin(theta)) / 2
        a = [area1 - area2, area2]
        print("%.6f %.6f" % (max(a), min(a)))


for line in sys.stdin:
    r, x, y = map(float, line.split())
    solve([x, y], r)
