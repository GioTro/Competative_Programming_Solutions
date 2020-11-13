# Solution to Encoded Message
import math, sys

def solve(s):
	n = int(math.sqrt(len(s)))
	square = []

	while len(s) > 0:
		square.append(s[:n][::-1])
		s = s[n:]

	string = ''

	while len(square[0]) > 0:
		for i in range(len(square)):
			string += square[i][0]
			square[i] = square[i][1:]

	return string


def read():
	return [line.strip() for line in sys.stdin][1:]

for answer in [solve(line) for line in read()]:
	print(answer)