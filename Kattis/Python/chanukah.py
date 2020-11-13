import sys

inp = list(sys.stdin)

for i in inp[1:]:
	index, days = map(int, i.split())
	print('%d %d' % (index, (days*(days + 1))/2 + days))