import sys
p, t = map(int, sys.stdin.readline().split())

count = 0
for i in range(p):
	s = ''
	for j in range(t):
		s += sys.stdin.readline()[1:]
	if s.lower() == s:
		count += 1

print(count)