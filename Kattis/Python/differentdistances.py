def solve(x1, y1, x2, y2, p):
	return (abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p)

l = [1]
while (l[0] != 0):
	l = list(map(float, raw_input().split()))
	if len(l) > 1:
		print(solve(l[0], l[1], l[2], l[3], l[4]))