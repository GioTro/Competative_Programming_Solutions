def mix(n, m):
    return [n / m, n % m, m]


while (a !=):
    a = list(map(int, raw_input().split()))
    if a == [0, 0]:
        break
    else:
        p = mix(a[0], a[1])
        print("{} {} / {}".format(p[0], p[1], p[2]))
