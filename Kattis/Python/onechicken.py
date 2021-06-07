n, m = map(int, input().split())

if n <= m:
    d = m - n
    s = 'piece'
    s += '' if d == 1 else 's'
    print('Dr. Chaz will have %d %s of chicken left over!' % (d, s))
else:
    d = n - m
    s = 'piece'
    s += '' if d == 1 else 's'
    print('Dr. Chaz needs %d more %s of chicken!' % (d, s))
