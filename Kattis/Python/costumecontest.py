def solve(l):
	category = []
	odds = []
	for i in l:
		if i not in category:
			category.append(i)
			count = 0
			for j in l:
				if i == j:
					count += 1
			odds.append(float(count)/len(l))
	res = []
	for i in range(len(odds)):
		if odds[i] == min(odds):
			res.append(category[i])
	return sorted(res)

def out(l):
	for i in l:
		print(i)

r = int(raw_input())
l = []
for i in range(r):
	l.append(str(raw_input()))

out(solve(l))