import sys


def area(a, b, h): return (a + b) / 2 * h / 1e3


inp = [list(map(float, i.split())) for i in sys.stdin]
to = int(inp[0][0])
inp = inp[1:]
answer = 0
for i in range(to - 1):
    x, y = inp[i]
    s, t = inp[i + 1]

    a, b = y, t
    h = s - x
    answer += area(a, b, h)
print(answer)
