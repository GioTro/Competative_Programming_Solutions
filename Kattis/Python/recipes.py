# Problem : https://open.kattis.com/problems/recipes

r = int(raw_input())
dash = ''
for i in range(40):
	dash += '-'

def solve(l, sf):
	res = []
	for item in l:
		if float(item[2]) == 100:
			sw = float(item[1])*sf
	for item in l:
		res.append([str(item[0]),str(float(item[2])*sw)])
	return res


for i in range(r):
	d = list(map(int, raw_input().split()))
	sf = float(d[2])/d[1]
	l = []
	for j in range(d[0]):
		l.append(list(map(str, raw_input().split())))
	l = solve(l, sf)

	# Print
	print("Recipe # %d" % (i+1))
	for item in l:
		print ("%s %.1f" % (str(item[0]), float(item[1])/100))
	print(dash)