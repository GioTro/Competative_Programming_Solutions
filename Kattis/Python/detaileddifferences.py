m = int(raw_input())

def seq(n, m, r):
	if len(n) == 0:
		return r
	else:
		if n[0] == m[0]:
			r += '.'
			return seq(n[1:], m[1:], r)
		else:
			r += '*'
			return seq(n[1:], m[1:], r)


for i in range(m):
	a = str(raw_input())
	b = str(raw_input())
	print("{}\n{}\n{}".format(a, b, seq(a, b, "")))