# Problem : https://open.kattis.com/problems/licensetolaunch
_ = input()
d = list(map(int, input().split()))
m, res = d[0], 0
for i in range(len(d)):
    g = m
    m = min(m, d[i])
    if g != m:
        res = i
print(res)
