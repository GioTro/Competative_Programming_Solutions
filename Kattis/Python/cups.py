# Problem : https://open.kattis.com/problems/cups
res = {}
for i in range(int(input())):
    s = list(map(str, input().split()))
    if s[0][0].islower():
        res.update({int(s[1]) * 2: s[0]})
    else:
        res.update({int(s[0]): s[1]})

for i in sorted(res.keys()):
    print(res[i])
