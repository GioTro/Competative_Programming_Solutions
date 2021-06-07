# Sum even Fibbonacci numbers below 4e6

a = 1
b = 2
c = 0
d = 0
e = 2

while b < 4000000:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        d += c
e += d

print(e)
