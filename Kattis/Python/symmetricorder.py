def solve(l, n):
	res1 = []
	res2 = []
	i = 0
	j = 0
	while (len(res1)+len(res2) < len(l)):
		if len(l[j]) == i and len(res1) == len(res2):
			res1.append(l[j])
		elif len(l[j]) == i:
			res2 = [l[j]]+res2

		if (j == len(l)-1):
			j = 0
			i += 1
		else:
			j += 1

	res = res1+res2
	print("SET %d" % n)
	for x in res:
		print(x)




r = int(raw_input())
n = 1
while (r != 0):
	l = []
	for i in range(r):
		l.append(str(raw_input()))
	l = solve(l, n)
	n += 1
	r = int(raw_input())
