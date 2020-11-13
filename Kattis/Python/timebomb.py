number = {
	"000":-1,
	"525":0,
	"005":1,
	"434":2,
	"335":3,
	"315":4,
	"433":5,
	"534":6,
	"115":7,
	"535":8,
	"435":9
}

def readp(l):
	res = []
	for i in range(0, len(l[0]), 4):
		r = []
		for j in range(3):
			s = ""
			for k in range(5):
				s += l[k][i+j]
			r.append(s)
		res.append(r)
	res2 = []

	for i in res:
		sl = []
		for j in i:
			r = 0
			for k in j:
				if k == '*':
					r += 1
			sl.append(r)
		res2.append(sl)

	return res2


def ind(s, t, i):
	if s == "434" and t[1][i*4] == '*':
		return "433"
	elif s in number.keys():
		return s
	else:
		return "000"


def solve(l, t):
	res = []
	for i in range(len(l)):
		s = ""
		for j in range(len(l[i])):
			s += str(l[i][j])
		res.append(number[ind(s, t, i)])

	if -1 in res:
		return "BOOM!!"
	
	s = ""
	for i in res:
		s += str(i)
	s = int(s)
	if s%6 == 0:
		return "BEER!!"
	else:
		return "BOOM!!"


l = []
for i in range(5):
	s = str(raw_input())
	s = s + ""
	l.append(s)

s = readp(l)
print(solve(s, l))
