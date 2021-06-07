import sys
import math


def toInt(a):
    return 26 if a == ' ' else (27 if a == '\'' else (ord(a) - ord('A')))


def fun(f, t):
    if f == t:
        return 0

    a = toInt(f)
    b = toInt(t)

    return min(a - b, (28 - a) + b) if b < a else min(b - a, (28 - b) + a)


inp = list(map(str, sys.stdin))
inp = inp[1:]
length = 2 * math.pi * (60 / 2) / 28

for s in inp:
    counter = 0

    for i in range(len(s) - 2):
        counter += fun(s[i], s[i + 1])

    print(counter * length / 15 + len(s) - 1)
