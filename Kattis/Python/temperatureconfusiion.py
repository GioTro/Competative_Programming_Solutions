# Problem : https://open.kattis.com/problems/temperatureconfusion
def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a


def solve(p, q):
    t, sign = 1337, 1
    if p < 0:
        sign *= -1
        p = abs(p)

    t = gcd(p, q)
    p /= t
    q /= t
    print("{}/{}".format(int(sign * p), int(q)))


p, q = map(int, input().split('/'))
p = 5 * (p - 32 * q)
q = 9 * q
solve(p, q)
