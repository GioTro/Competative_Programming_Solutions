i = int(input())
if i == 1:
	print('Either')
else:
	if i % 2 == 0:
		if (i/2) % 2 == 1:
			print('Odd')
		else:
			print('Even')
	else:
		print('Either')