# Problem : https://open.kattis.com/problems/sumkindofproblem

def solve(n):
	s1, s2, s3, i = 0, 0, 0, 1

	while (True):
		if (i <= n):
			s1 += i
		if (i % 2 == 1 and i <= 2*n):
			s2 += i
		if (i % 2 == 0 and i <= 2*n):
			s3 += i
		if (i > 2*n):
			break
		i += 1
	return [s1, s2, s3]

r = int(raw_input())

for i in range(r):
	p, q = map(int, raw_input().split())
	k = solve(q)
	print("{} {} {} {}".format(p, k[0], k[1], k[2]))