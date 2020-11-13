# Problem : https://open.kattis.com/problems/whatdoesthefoxsay
import re
p = int(raw_input())
for i in range(p):
	s = str(raw_input())
	t, d = "", ""
	while True:
		t = str(raw_input())
		if t == 'what does the fox say?':
			break
		else:
			d += t+" "
	d = re.findall('goes [a-z]+', d)
	t = []
	for i in d:
		_, p = map(str, i.split())
		t.append(p)
	s = list(s.split())
	while len(t) > 0:
		while t[0] in s:
			s.remove(t[0])
		t = t[1:]

	print(" ".join(s).strip())

