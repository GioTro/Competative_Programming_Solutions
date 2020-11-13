# Equilibrium Mobile
import re, math

def solve(tokens):
	depth = 0
	seen  = 0
	count = {}

	for token in tokens:
		#print(token)
		if token == '[':
			depth += 1
		elif token == ']':
			depth -= 1
		elif token == ',':
			pass
		else:
			seen += 1
			try:
				## same as int(token)*2**depth
				count[int(token) << depth] += 1
			except:
				count[int(token) << depth] = 1

	mx = 0
	for number in count.values():
		mx = max(mx, number)
	write((seen - mx))

def parse(s):
	regex 			= '0*[1-9][0-9]*|\[|\]|,'
	pattern = re.compile(regex)
	return pattern.findall(s) # Generate tokens

def write(out):
	print(out)

def read():
	tokens = parse(str(input()))
	solve(tokens)


if __name__ == '__main__':
	do = int(input())
	while do > 0:
		read()
		do -= 1