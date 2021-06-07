import sys

inp = [list(map(int, i.split())) for i in sys.stdin]

N, Q = inp[0]
location = inp[1]

for i in inp[2:]:
    a, b, c = i
    if a == 1:
        location[b - 1] = c
    if a == 2:
        print(abs(location[b - 1] - location[c - 1]))
