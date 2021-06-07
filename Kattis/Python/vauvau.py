# Brute
import sys

a, b, c, d = map(int, sys.stdin.readline().split())
p, m, g = map(int, sys.stdin.readline().split())

dog_1 = []
dog_2 = []

d_1 = a - 1
d_2 = c - 1

for i in range(max([p, m, g])):
    if d_1 >= 0:
        dog_1.append(True)
        d_1 -= 1
    else:
        dog_1.append(False)
        d_1 -= 1

    if d_1 == -b - 1:
        d_1 = a - 1

    if d_2 >= 0:
        dog_2.append(True)
        d_2 -= 1
    else:
        dog_2.append(False)
        d_2 -= 1

    if d_2 == -d - 1:
        d_2 = c - 1

for i in [p, m, g]:
    if (dog_1[i - 1] and dog_2[i - 1]):
        print('both')
    elif (dog_1[i - 1] ^ dog_2[i - 1]):
        print('one')
    else:
        print('none')

print(dog_1, dog_2)
