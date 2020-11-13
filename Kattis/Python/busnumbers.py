def solve(l):
    res = [[l[0]]]
    for i in l[1:]:
        if res[-1][-1] == i-1:
            res[-1].append(i)
        else:
            res.append([i])
    s = ''
    for i in res:
        if len(i) > 2:
            s += str(i[0])+'-'+str(i[-1])+' '
        else:
            t = [j for j in i]
            for j in t:
                s += str(j)+' '
    return s.strip()
        

_ = input()
s = list(map(int, input().split()))
print(solve(sorted(s)))
