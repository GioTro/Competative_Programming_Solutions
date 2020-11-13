# Solution for Kattis problem: https://open.kattis.com/problems/trilemma

import math

def toCord(n):
    return [[n[0], n[1]], [n[2], n[3]], [n[4], n[5]]]

def colinear(n, m, p):
    res = n[0]*(m[1]-p[1]) + m[0]*(p[1]-n[1]) + p[0]*(n[1]-m[1])
    if res == 0:
        return True
    else:
        return False

def dotproduct(n, m):
    res = 0
    for i in range(0, len(n)):
        res += n[i]*m[i]
    return res

def distance(n, m):
    v = [n[0]-m[0], n[1]-m[1]]
    return dotproduct(v, v)

def check(p):
    res = ""
    dis = [distance(p[0], p[1]), distance(p[1], p[2]), distance(p[2], p[0])]
    dis = sorted(dis)

    if (colinear(p[0], p[1], p[2])):
        return "not a triangle"

    if dis[0] == dis[1] or dis[1] == dis[2]:
        res += "isosceles "
    else:
        res += "scalene "

    if ((dis[0]+dis[1]) > dis[2]):
        res += "acute triangle"
    elif ((dis[0]+dis[1]) == dis[2]):
        res += "right triangle"
    else:
        res += "obtuse triangle"
    return res


cases = int(input())
points = []
for i in range(0, cases):
    read = list(map(int, input().split()))
    points.append(toCord(read))

for i in range(0, cases):
    print("Case #{}: {}".format(i+1, check(points[i])))