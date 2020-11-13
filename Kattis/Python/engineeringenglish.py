# Problem : https://open.kattis.com/problems/engineeringenglish
import sys
s = []

for line in sys.stdin:
	s.append(str(line).lower())

seen = []
for i in s:
	t = list(i.split())
	st = ""
	for j in t:
		if j not in seen:
			st += j + " "
			seen.append(j)
		else:
			st += ". "

	print(st.strip())


	