# Problem : https://open.kattis.com/problems/prva 

def solve(l, r, c):
	t = []
	for i in range(c):
		s = ""
		for j in range(r):
			s += l[j][i]
		t.append(s)
	res = []

	for i in t:
		res = res+list(i.split('#'))
	for i in l:
		res = res+list(i.split('#'))
	t = []
	for i in res:
		if len(i) >= 2:
			t.append(i)

	return sorted(t)[0]


a, b = map(int, raw_input().split())
l = []
	
for j in range(a):
	l.append(str(raw_input()))

print(solve(l, a, b))

