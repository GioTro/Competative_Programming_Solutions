def solve(s, a, b, c, ag, bs, cs, at, bt, ct):
	if (len(s) == 0):
		p([a, b, c], ["Adrian", "Bruno", "Goran"])
		return
	if (len(ag) == 0):
		ag = at	
	if (len(bs) == 0):
		bs = bt
	if (len(cs) == 0):
		cs = ct
	if (s[0] == ag[0]):
		a += 1
	if (s[0] == bs[0]):
		b += 1
	if (s[0] == cs[0]):
		c += 1

	solve(s[1:], a, b, c, ag[1:], bs[1:], cs[1:], at, bt, ct)

def p(l, d):
	t = max(l[0], max(l[1], l[2]))
	print(t)
	for i in range(len(l)):
		if (l[i] == t):
			print(d[i])


s = raw_input()
s = str(raw_input())

a, b, c = 0, 0, 0
ag = "ABCABC"
bs = "BABC"
cs = "CCAABB"
solve(s, a, b, c, ag, bs, cs, ag, bs, cs)