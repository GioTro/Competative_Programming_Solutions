# Using expected value
import sys

sh = lambda a : a*(a + 1)/2
s = lambda a, b : sh(b) - (0 if a == 1 else sh(a - 1))
ev = lambda a1, b1, a2, b2 : s(a1, b1)/(b1 - a1 + 1) + s(a2, b2)/(b2 - a2 + 1)

inp = [list(map(int, line.split())) for line in sys.stdin]

g = ev(*inp[0])
e = ev(*inp[1])

print('Emma' if e > g else 'Gunnar' if g > e else 'Tie')