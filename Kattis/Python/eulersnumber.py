def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


def solve(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n > 15:
        return 2.718281828458995

    t = float(fac(n))
    res = 1 / t + 2

    while n > 2:
        t = t / n
        n = n - 1
        res += 1 / t

    return res


print(solve(int(input())))
