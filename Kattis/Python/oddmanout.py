# Problem : https://open.kattis.com/problems/oddmanout

def solve(n):
	d = sorted(n)
	for i in range(0 ,len(n)-1 ,2):
		if d[i] != d[i+1]:
			return d[i]
	return d[-1]

r = int(raw_input())

for i in range(r):
	d = int(raw_input())
	d = list(map(int, raw_input().split()))
	print("Case #%d: %d" % (i+1, solve(d)))