# Problem : https://open.kattis.com/problems/cetiri

r = sorted(list(map(int, raw_input().split())))
u = r[2] - r[1]
v = r[1] - r[0]

if u == v:
    print(r[2] + abs(u))
elif u > v:
    print(r[1] + abs(v))
else:
    print(r[0] + abs(u))
