import sys

inp = [list(map(int, line.split())) for line in sys.stdin]
A, B, C = inp[0]
tr_1 = inp[1]
tr_2 = inp[2]
tr_3 = inp[3]

e = max(tr_1[1], max(tr_2[1], tr_3[1]))

sigma = 0

for i in range(1, e+1):
	count = 0
	if tr_1[0] <= i < tr_1[1]:
		count += 1
	if tr_2[0] <= i < tr_2[1]:
		count += 1
	if tr_3[0] <= i < tr_3[1]:
		count += 1
	sigma += 0 if count == 0 else (A if count == 1 else (B*2 if count == 2 else C*3))
print(sigma)
