def solve(n, b):
	if n[0] + n[1] == n[2]:
		if b:
			print("%d+%d=%d" % (n[0], n[1], n[2]))
		else:
			print("%d=%d+%d" % (n[2], n[0], n[1]))
		return

	if n[0] - n[1] == n[2]:
		if b:
			print("%d-%d=%d" % (n[0], n[1], n[2]))
		else:
			print("%d=%d-%d" % (n[2], n[0], n[1]))
		return

	if n[0] * n[1] == n[2]:
		if b:
			print("%d*%d=%d" % (n[0], n[1], n[2]))
		else:
			print("%d=%d*%d" % (n[2], n[0], n[1]))
		return

	if n[0] / n[1] == n[2]:
		if b:
			print("%d/%d=%d" % (n[0], n[1], n[2]))
		else:
			print("%d=%d/%d" % (n[2], n[0], n[1]))
		return

	return solve([n[1], n[2], n[0]], False)

d = list(map(int, raw_input().split()))
solve(d, True)