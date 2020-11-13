def solve(l1, l2):
	t1, t2 = sorted(l1), sorted(l2)
	d = {}
	for i in range(len(l1)):
		d[t1[i]] = t2[i]

	for i in l1:
		print(str(d[i]))

r = 1
while (r != 0):
	r = int(raw_input())
	l1, l2 = [], []
	for i in range(r):
		l1.append(int(raw_input()))
	for i in range(r):
		l2.append(int(raw_input()))
	solve(l1, l2)
	print("")

	