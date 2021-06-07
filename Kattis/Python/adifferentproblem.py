import sys


def solve(n):
    print(abs(n[1] - n[0]))


for line in sys.stdin:
    solve(list(map(int, line.split())))
