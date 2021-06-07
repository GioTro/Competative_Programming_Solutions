def solve(l, t):
    count = 0
    j = 0
    for i in l:
        count += i
        j += 1
        if count > t:
            return j - 1
    return len(l)


_, t = map(int, raw_input().split())
d = list(map(int, raw_input().split()))

if d[0] > t:
    print(0)
else:
    print(solve(d, t))
