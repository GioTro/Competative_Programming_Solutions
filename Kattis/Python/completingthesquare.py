# Problem : https://open.kattis.com/problems/completingthesquare
def dot(u, v):
    return u[0]*v[0]+u[1]*v[1]
def summa(r):
    x1, x2 = 0, 0
    for i in r:
        x1 += i[0]
        x2 += i[1]
    return [x1, x2]


def solve(l):
    s = []
    for i in l:
        u, v = [-i[0], -i[1]], [-i[0], -i[1]]
        boo = False
        for j in l:
            if j != i:
                if boo:
                    v = [v[0]+j[0], v[1]+j[1]]
                else:
                    u = [u[0]+j[0], u[1]+j[1]]
                    boo = True
        if dot(u, v) == 0:
            s = i
            break
    r = [s]+[[i[0]-s[0], i[1]-s[1]] for i in l if i != s]
    return summa(r)
                
                
    
d = [list(map(int, input().split())) for _ in range(3)]
d = solve(d)
print("{} {}".format(d[0], d[1]))
