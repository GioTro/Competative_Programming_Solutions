def solve(l, d):
	for i in range(len(l)):
		if l[i] <= d:
			return "It hadn't snowed this early in {} years!".format(i)
	return "It had never snowed this early!"

n, d = map(int, raw_input().split())
l = list(map(int, raw_input().split()))
print(solve(l, d))