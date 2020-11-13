def solve(n):
	res = [0, 0, 0, 0]
	le = len(n)
	for i in range(len(n)):
		c = ord(n[i])
		if c >= 97 and c <= 122:
			res[1] += 1
		elif c >= 65 and c <= 90:
			res[2] += 1
		elif c == 95:
			res[0] += 1
		else:
			res[3] += 1
	return [float(res[0])/le, float(res[1])/le, float(res[2])/le, float(res[3])/le]


d = str(raw_input())
d = solve(d)
print( "{}\n{}\n{}\n{}".format(d[0], d[1], d[2], d[3]) )