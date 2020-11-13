def solve(n):
	max = 0
	for i in range(len(n)):
		c = n[i][0]
		hold = 0
		for j in range(len(n)):
			if c == n[j][0]:
				hold += 1
		if hold > max:
			max = hold
	return max


print(solve(list(map(str, raw_input().split()))))
