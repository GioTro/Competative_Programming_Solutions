import sys

shift = lambda c1, c2 : chr(((c1 - c2) % 26) + ord('A'))
s1, s2 = list(map(str.strip, sys.stdin))
s1 = list(s1)

for i in range(len(s1)):
	if i % 2 == 0:
		s1[i] = shift(ord(s1[i]) - ord('A'), ord(s2[i]) - ord('A'))
	else:
		s1[i] = shift(ord(s1[i]) - ord('A'), -(ord(s2[i]) - ord('A')))

print(''.join(s1))