import math, sys

f = lambda D, V : (D**3 - 6*V/math.pi)**(1/3)

for i in sys.stdin:
	d, v = map(int, i.split())
	
	if d == v == 0:
		continue

	print(f(d, v))