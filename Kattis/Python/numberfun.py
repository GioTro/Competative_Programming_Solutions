def solve(p, q, s):
	a = "Possible"
	if (p + q == s):
		return a
	if (p - q == s or q - p == s):
		return a
	if (p*q == s):
		return a
	if (float(p)/q == s or float(q)/p == s):
		return a

	return "Impossible"

r = int(raw_input())

for i in range(r):
	p, q, s = map(int, raw_input().split())
	print(solve(p, q, s))