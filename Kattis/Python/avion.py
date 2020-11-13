import sys

answers = [('FBI' in line) for line in sys.stdin]
out = ''
index = 1

for a in answers:
	if a:
		out += str(index) + ' '
	index += 1

if out == '':
	print('HE GOT AWAY!')
else:
	print(out)