import sys

def do(x, y):
	next = lambda n : int(n/2) if n%2 == 0 else (3*n + 1)
	x_0, y_0, step = x, y, 0

	dic = {x:0}

	while x != 1:
		x = next(x)
		step += 1
		dic[x] = step

	step = 0

	while y != 1:
		if y in dic.keys():
			break
		else:
			y = next(y)
			step += 1

	print('%d needs %d steps, %d needs %d steps, they meet at %d' % (x_0, dic[y], y_0, step, y))

for line in sys.stdin:
	x, y = map(int, line.split())
	
	if x == y == 0:
		pass
	else:
		do(x, y)