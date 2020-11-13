s = input().strip()

while len(s) % 3 != 0:
	s = '0' + s

p = ''
while len(s):
	p += str(int(s[:3], base = 2))
	s = s[3:]
print(p)
