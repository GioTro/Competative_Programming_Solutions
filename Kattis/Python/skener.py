import sys

def read():
	inp = list(sys.stdin)
	r, c, z_r, z_c = map(int, inp[0].split())
	inp = [[c for c in s] for s in inp[1:]]
	return (r, c, z_r, z_c, inp)

def do(r, c, z_r, z_c, arr):
	array = [['' for j in range(c*z_c)] for i in range(r*z_r)]
	for row in range(r):
		for col in range(c):
			for row_k in range(z_r):
				for col_k in range(z_c):
					array[row*z_r + row_k][col*z_c + col_k] = arr[row][col]
	return array

def write(arr):
	for row in arr:
		print(''.join(row))

write(do(*read()))
