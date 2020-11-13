## HangingOut
import sys
def solve(n, events):
	count = 0
	current = 0

	for event in events:
		e, g = event.split()
		g = int(g)

		if e == 'leave':
			current -= g
		else:
			if (current + g) > n:
				count += 1
			else:
				current += g

	write(count)

def write(s):
	print(s)

def read():
	inp = [line.strip() for line in sys.stdin]
	solve(int(inp[0].split()[0]), inp[1:])
	
read()