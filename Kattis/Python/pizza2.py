import math, sys
f = lambda r, c : (math.pi*(r - c)**2)/(math.pi*r**2)*100
r, c = map(int, input().split())
print(f(r, c))