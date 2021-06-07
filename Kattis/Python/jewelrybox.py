def solve(x, y, l, h):
    if h - l < 10e-7:
        return l

    t0 = l + (h - l) / 3
    t1 = l + (h - l) * 2 / 3
    if t0 * (x - t0 * 2) * (y - t0 * 2) > t1 * (x - t1 * 2) * (y - t1 * 2):
        return solve(x, y, l, t1)
    else:
        return solve(x, y, t0, h)


r = int(input())

for _ in range(r):
    x, y = map(int, input().split())
    a = solve(x, y, 0, min(x, y) / 2)
    print(a * (x - 2 * a) * (y - 2 * a))
