def sumDigits(n):
	n = str(n)
	res = 0
	for i in range(len(n)):
		res += int(n[i])
	return res

def solve(n):
	if n%sumDigits(n) == 0:
		return n
	else:
		return solve(n+1)

print(solve(int(raw_input())))

