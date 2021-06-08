# Solution for Kattis Problem: https://open.kattis.com/problems/zamka
# Linear solution

a = int(input())
b = int(input())
c = int(input())


def sumDigits(integer, z):
    s = str(integer)
    summa = 0
    for i in range(0, len(s)):
        summa += int(s[i])
    if summa == z:
        return True
    else:
        return False


result = []
for i in range(a, b + 1):
    if sumDigits(i, c):
        result.append(i)
    else:
        continue

print(result[0])
print(result[-1])
