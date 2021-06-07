stars = int(input())
ceil = int((stars / 2) + (1 if stars % 2 == 0 else 2))

print('%d:' % (stars))

for i in range(2, ceil):
    n = stars % (i * 2 - 1)

    if n == i or n == 0:
        print('%d,%d' % (i, i - 1))

    if stars % i == 0:
        print('%d,%d' % (i, i))
