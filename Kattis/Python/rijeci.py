lim = int(input())
a, b = 1, 0
while lim > 0:
    t = b
    b = a + b
    a = t
    lim -= 1

print("%d %d" % (a, b))
