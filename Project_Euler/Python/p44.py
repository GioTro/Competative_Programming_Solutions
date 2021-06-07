# Search is very slow
# very very very slow

import time
start = time.time()

hexagonal = []


def pen(number):
    value = int(number) * (3 * int(number) - 1) / 2
    return int(value)


def summat(number1, number2):
    su = number1 + number2
    return int(su)


def differens(number1, number2):
    differens = abs(number1 - number2)
    return differens


for i in range(1, 100000):
    hexagonal.append(pen(i))

summa = set()
differens = set()

for i in range(0, len(hexagonal)):
    for j in range(i, len(hexagonal)):
        x, y = int(hexagonal[i]), int(hexagonal[j])
        value1 = x + y
        value2 = abs(x - y)
        if value1 in hexagonal:
            summa.add(value1)
        if value2 in hexagonal:
            differens.add(value2)


if x in differens and summa:
    x = x
    print(x)


elapsed = time.time() - start

print(elapsed)
