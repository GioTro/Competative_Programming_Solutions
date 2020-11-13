r = int(raw_input())

for i in range(r):
	n, d = map(str, raw_input().split())
	p, q = map(int, d.split('/'))

	seq = []
	while (p != 1 or q != 1):
		if (p > q):
			p -= q
			seq.append('1')
		else:
			q -= p
			seq.append('0')
	seq.append('1')
	print("%d %d" % (int(n), int(''.join(seq[::-1]), base=2)))