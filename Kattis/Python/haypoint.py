# Problem : https://open.kattis.com/problems/haypoints
def solve(s):
    res = 0
    l = list(map(str, s.split()))
    for i in l:
        if i in dic:
            res += dic[i]
    return res


dic = {}
p, q = map(int, input().split())
for _ in range(p):
    h, t = map(str, input().split())
    dic.update({h: int(t)})

for _ in range(q):
    t = str(input())
    s = t + " "
    while t != '.':
        t = str(input())
        s += t + " "
    print(solve(s))
