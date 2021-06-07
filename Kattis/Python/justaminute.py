r = int(input())
i, j = 0, 0
for _ in range(r):
    p, q = map(float, input().split())
    p *= 60
    i += p
    j += q
if j / i <= 1:
    print('measurement error')
else:
    print('{:.8f}'.format(j / i))
