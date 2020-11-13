def d2array(row, columns):
	l = []
	for i in range(row):
		r = []
		for j in range(columns):
			r.append(-1)
		l.append(r)
	return l

def toInt(c):
	return ord(c)-97

def toAlpha(n):
	return str(unichr(n+97))

def numPos(n):
	res = []
	if n-1 > 0:
		res.append(str(n-1))
	if n+1 <= 8:
		res.append(str(n+1))
	return res

def alphaPos(n):
	res = []
	if toInt(n)-1 >= 0:
		res.append(toAlpha(toInt(n)-1))
	if toInt(n)+1 < 8:
		res.append(toAlpha(toInt(n)+1))
	return res

def nextPos(s):
	res = []

	if (toInt(s[0])+2 < 8):
		t = toAlpha(toInt(s[0])+2)
		l = numPos(int(s[1]))
		for i in l:
			if int(i) > 0 and int(i) < 8:
				res.append(t+i)

	if (toInt(s[0]) - 2 >= 0):
		t = toAlpha(toInt(s[0])-2)
		l = numPos(int(s[1]))
		for i in l:
			if int(i) > 0 and int(i) < 8:
				res.append(t+i)

	if (int(s[1]) + 2 <= 8):
		t = str(int(s[1])+2)
		l = alphaPos(s[0])
		for i in l:
			if toInt(i) >= 0 and toInt(i) < 8:
				res.append(i+t)

	if (int(s[1]) - 2 > 0):
		t = str(int(s[1])-2)
		l = alphaPos(s[0])
		for i in l:
			if toInt(i) >= 0 and toInt(i) < 8:
				res.append(i+t)

	return sorted(res)

def mark(s, n, l):
	if l[toInt(s[0])][int(s[1]) - 1] >= n or l[toInt(s[0])][int(s[1]) - 1] == -1:
		l[toInt(s[0])][int(s[1]) - 1] = n

def solve(s, n, array, seen):
	while (len(seen) < 64):
		l = []
		for i in s:
			if i not in seen:
				seen.append(i)
				mark(i, n, array)
				t = nextPos(i)
				for j in t:
					if j not in seen:
						l.append(j)
		s = l
		n += 1
	return array

def out(l):
	res = 0
	for i in l:
		if max(i) > res:
			res = max(i)
	d = []
	for i in range(8):
		for j in range(8):
			if l[i][j] == res:
				d.append("{}{}".format(toAlpha(i), str(j+1)))

	s = "{}".format(res)
	for i in range(8):
		t = []
		for j in d:
			if int(j[1]) == 8 - i:
				t.append(j)
		t = sorted(t)
		for j in t:
			s += " {}".format(j)

	return s





# test = sorted(["b6", "b4", "c3", "e3", "f4", "f6", "c7", "e7"])
# print(test == nextPos("d5"))
# test = sorted(["b6", "c7"])
# print(test == nextPos("a8"))
# test = sorted(["c2", "b3"])
# print(test == nextPos("a1"))

r = int(raw_input())
for i in range(r):
	d = [str(raw_input())]
	print(out(solve(d, 0, d2array(8, 8), [])))