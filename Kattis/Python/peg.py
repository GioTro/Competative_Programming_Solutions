import sys
inp = [list(line)[:-1] for line in sys.stdin]

count = 0
for row in range(7):
	for col in range(7):
		if inp[row][col] == '.':
			if row - 2 >= 0:
				if inp[row - 1][col] == 'o' and inp[row - 2][col] == 'o':
					count += 1

			if row + 2 < 7:
				if inp[row + 1][col] == 'o' and inp[row + 2][col] == 'o':
					count += 1

			if col - 2 >= 0:
				if inp[row][col-1] == 'o' and inp[row][col - 2] == 'o':
					count += 1

			if col + 2 < 7:
				if inp[row][col + 1] == 'o' and inp[row][col + 2] == 'o':
					count += 1

print(count)
