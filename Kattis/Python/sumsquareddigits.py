# Problem : https://open.kattis.com/problems/sumsquareddigits
def base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

for i in range(int(input())):
    p, q, r = map(int, input().split())
    p = base(r, q)
    res = 0
    for j in p:
        res += j**2
    print('{} {}'.format(i+1, res))
    

