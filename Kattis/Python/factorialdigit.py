def fact(n):
	if (n == 1):
		return 1
	else:
		return n*fact(n-1)%10

n = int(raw_input())

for i in range(n):
	print(fact(int(raw_input())))