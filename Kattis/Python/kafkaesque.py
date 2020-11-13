import sys

inp = list(sys.stdin)[1:]

count = 1
previous = -1

while len(inp):
	if int(inp[0]) > previous:
		previous = int(inp.pop(0))
	else:
		count += 1
		previous = -1

print(count)