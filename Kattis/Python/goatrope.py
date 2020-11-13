# Problem : https://open.kattis.com/problems/goatrope
import math
def corners(p1, p2):
    return [p1, p2, (p1[0], p2[1]), (p2[0], p1[1])]

def pyth(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def hypot(c, p):
    return [pyth(p, i) for i in c]
    
x, y, x1, y1, x2, y2 = map(int, input().split())
if x1 <= x <= x2:
    print(min(abs(y1 - y), abs(y - y2)))
elif y1 <= y <= y2:
    print(min(abs(x1 - x), abs(x - x2)))
else:
    print(min(hypot(corners((x1, y1), (x2, y2)), (x, y))))
