# Problem : https://open.kattis.com/problems/simon
import re
p = int(input())
for _ in range(p):
	line = str(input())
	l = re.findall('simon says', line)

	if len(l) == 0:
		print('\n')
	elif line[:10] != 'simon says':
		print('\n')
	else:
		print(line[11:])
