# Problem : https://open.kattis.com/problems/touchscreenkeyboard

seen = {}
def distance(c1, c2):
    if c1 == c2:
        return 0

    if (c1+c2) in seen.keys():
        return seen[c1+c2]
    if (c2+c1) in seen.keys():
        return seen[c2+c1]
    
    keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

    rows, hor = [[], []], 0
    for i in keyboard:
        if c1 in i:
            hor += keyboard.index(i)
            rows[0] = i
        if c2 in i:
            hor -= keyboard.index(i)
            rows[1] = i
    r = (abs(hor) + abs(rows[0].index(c1) - rows[1].index(c2)))
    seen.update({c1+c2 : r})
    seen.update({c2+c1 : r})
    return (abs(hor) + abs(rows[0].index(c1) - rows[1].index(c2)))
            
        
def solve(s, l):
    res = []
    for i in l:
        d = 0
        for j in range(len(s)):
            d += distance(i[j], s[j])
        res.append([i, str(d)])
    return res

def resolve(l, n):
    res = []
    for i in l:
        res.append(i[0])
    for i in sorted(res):
        print("{} {}".format(str(i), str(n)))

p = int(input())
for _ in range(p):
    s, q = map(str, input().split())
    l = []
    for i in range(int(q)):
        l.append(str(input()))

    order = []
    res = solve(s, l)
    for i in res:
        order.append(int(i[1]))

    for i in sorted(set(order)):
        l = []
        for j in res:
            if int(j[1]) == i:
                l.append(j)
        if (len(l)) == 1:
            print("{} {}".format(l[0][0], l[0][1]))
        else:
            resolve(l, i)
                
