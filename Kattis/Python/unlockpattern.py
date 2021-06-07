# Problem : https://open.kattis.com/problems/unlockpattern

import math


def length(v):
    return math.sqrt(v[0]**2 + v[1]**2)


def solve(l):
    index, res = 1, 0
    while True:
        x = l.index(index)
        y = l.index(index + 1)
        res += length([(x % 3 + 1) - (y % 3 + 1),
                       (int(x / 3) + 1) - (int(y / 3) + 1)])
        index += 1
        if index == 9:
            break
    return res


d = []
for _ in range(3):
    m = list(map(int, input().split()))
    for i in m:
        d.append(i)
print(solve(d))
