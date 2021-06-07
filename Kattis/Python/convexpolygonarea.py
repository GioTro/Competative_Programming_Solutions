def structure(l):
    x, y = [], []
    for i in range(0, len(l) - 1, 2):
        x.append(l[i])
        y.append(l[i + 1])
    return [x, y]


def summa(m, n):
    res = 0
    for i in range(len(m)):
        res += m[i] * n[i]
    return res


def determinant(r, c):
    m = r + [r[0]]
    n = c + [c[0]]
    return float(summa(r, n[1:]) - summa(m[1:], c))


def solve(l):
    return determinant(l[0], l[1]) / 2


r = int(raw_input())

for i in range(r):
    l = list(map(int, raw_input().split()))
    print(solve(structure(l[1:])))
