# Problem : https://open.kattis.com/problems/flowlayout
def solve(l, w):
    wa, wp, h, hp, j = 0, 0, 0, 0, 0
    for i in l:
        if (wp+i[0]) > w:
            h += hp
            wa = max(wa, max(i[0], wp))
            wp, hp = i[0], i[1]
        else:
            wp = wp + i[0]
            hp = max(hp, i[1])
    wa = max(wa, wp)
    h += hp
    return "{} x {}".format(wa, h)

while True:
    l = []
    w = int(input())
    if w == 0:
        break
    
    while True:
        p, q = map(int, input().split())
        if p == -1 and q == -1:
            break
        else:
            l.append([p, q])
    print(solve(l, w))
    
    
