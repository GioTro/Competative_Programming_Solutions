p, n = map(int, raw_input().split())
l = []
for i in range(n):
	l.append(str(raw_input()))

s = list(set(l))
if len(s) < p:
	print("paradox avoided")
s = []
for i in range(len(l)):
	if l[i] not in s:
		s.append(l[i])
	if len(s) == p:
		print(i+1)
		break
