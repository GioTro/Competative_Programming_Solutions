# Problem : https://open.kattis.com/problems/sodasurpler
e, f, c = map(int, input().split())
res, e = 0, e+f
while (e - c >= 0):
    res += 1
    e -= c
    e += 1
print(res)
