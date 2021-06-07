import sys

inp = list(sys.stdin)
inp = inp[1:]

for line in inp:
    seq = list(map(int, line.split()))
    x = seq[0]
    seq = seq[1:]
    answer = 0
    for num in seq:
        x = x * 2
        answer += num - x if num > x else 0
        x = num
    print(answer)
