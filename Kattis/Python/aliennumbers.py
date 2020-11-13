#https://open.kattis.com/problems/aliennumbers

def decimal2n(n, b):
	res = ''
	num = len(b)
	c = int(n)
	while c > 0:
		rem = c % num
		res = b[rem] + res
		c /= num
	return res

def n2decimal(n, b):
	num = 0
	for i in range(len(n)):
		num = len(b)*num + b.index(n[i])
	return num

def solve(d):
	return decimal2n(n2decimal(d[0], d[1]), d[2])

r = int(raw_input())
for i in range(r):
	d = list(map(str, raw_input().split()))
	print("Case #{}: {}".format(i+1, solve(d)))
