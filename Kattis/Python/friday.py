r = int(raw_input())

def solve(d):
	cd = 6
	res = 0
	for i in range(len(d)):
		for j in range(d[i]):
			if (j+1) == 13 and (cd % 7) == 4:
				res += 1
			cd += 1
	return res

for i in range(r):
	throw = list(map(int, raw_input().split()))
	l = list(map(int, raw_input().split()))
	print(solve(l))
