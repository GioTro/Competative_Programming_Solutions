# Problem : https://open.kattis.com/problems/soylent
def solve(n):
	res = 0
	i = 0
	while ( res < n ):
		i += 1
		res = i*400
	return i


r = int(raw_input())

for i in range(r):
	d = int(raw_input())
	print(solve(d))