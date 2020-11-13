a, b = input().split()

array = [['.' for i in range(len(a))] for j in range(len(b))]

row = col = -1

for i in a:
	if i in b:
		row = b.index(i)
		col = a.index(i)
		break

array[row] = list(a)

for i in range(len(b)):
	array[i][col] = b[i]

for row in array:
	print(''.join(row))