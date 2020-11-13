r = int(raw_input())
res = 0.0
for i in range(r):
    d = list(map(float, raw_input().split()))
    res += d[0]*d[1]

print("%.3f" % res)
