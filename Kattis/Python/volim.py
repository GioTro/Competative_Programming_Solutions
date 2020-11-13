import sys
inp = list(sys.stdin)
p = int(inp[0]) - 1
inp = inp[2:]

time = 0
e = 3*60 + 30

for line in inp:
	t, a = line.split()
	time += int(t)
	if time >= e:
		break
	else:
		if a == 'T':
			p += 1

print((p%8) + 1)