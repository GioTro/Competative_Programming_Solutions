# Problem : https://open.kattis.com/problems/iboard
import sys


def solve(s):
    left, right, sequence = True, True, "".join(
        [bin(ord(i))[2:].zfill(7)[::-1] for i in s])
    for i in sequence:
        if i == '1':
            left = not left
        else:
            right = not right
    return 'free' if (left and right) else 'trapped'


for line in sys.stdin.readlines():
    print(solve(line[:-1]))
