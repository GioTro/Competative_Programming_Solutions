def average(n):
	l = float(sum(n))/len(n)
	count = 0
	for i in n:
		if i > l:
			count += 1
	return float(count)/len(n)

r = int(raw_input())

for i in range(r):
	a = list(map(int, raw_input().split()))
	print("{}%".format(str.format('{0:.3f}', average(a[1:])*100)))
