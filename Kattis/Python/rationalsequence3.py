import sys

def do(q):
	stack = []

	while q != 1:
		if (q%2 == 1):
			stack.append(0)
		else:
			stack.append(1)
		q = int(q/2)

	stack = stack[::-1]
	n = d = 1
	while len(stack):
		if stack.pop(0):
			d += n
		else:
			n += d

	return '{}/{}'.format(n, d)

sys.stdin.readline()

for line in sys.stdin:
	p, q = map(int, line.split())
	print('%d %s' % (p, do(q)))