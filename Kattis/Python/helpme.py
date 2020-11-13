# Not finished need to fix for this stupid formating
# And clean up la mess i.e E*V*E*R*Y*T*H*I*N*G ;)
# hashtag didn't go as planned

def read(b):
	white, black = [], []
	row = 8
	for i in b:
		column = 'a'
		i = '**'+i+'**' # Adds padding
		for j in range(1,9):
			if i[j*4] in ['K', 'Q', 'R', 'B', 'N', 'P']:
				white.append(i[j*4]+str(row)+column)
			if i[j*4] in ['k', 'q', 'r', 'b', 'n', 'p']:
				black.append(i[j*4]+str(row)+column)
			column = chr(ord(column)+1)
		row -= 1
	return [white, black]


def revert(l):
	ret = []
	for i in l:
		if len(i) == 2:
			ret.append(i[1]+i[0])
		else:
			ret.append(i[0]+i[2]+i[1])
	return ret

def revertBlack(l):
	print("I'm fucked")
	return l

def resolve(l, white):
	rank = ['K', 'Q', 'R', 'B', 'N']
	ret = []
	while len(rank) > 0:
		temp = []
		for i in l:
			print(l)
			if i[0].upper() == rank[0]:
				temp.append(i[0].upper()+i[1:])

		if white:
			ret += sorted(temp)
		else:
			ret += reversed(sorted(temp))
		rank = rank[1:]

	temp = []
	for i in l:
		if i[0].upper() == 'P':
			temp.append(i[1:])
	if white:
		ret += sorted(temp)
	else:
		ret += sorted(temp)
	return revert(ret) if white else revertBlack(ret)


board = []

for i in range(17):
	if i%2 == 0:
		input()
		continue
	else:
		board.append(str(input()))

t = read(board)
print(t[0])
white = resolve(t[0], True)
black = resolve(t[1], False)
print(white, black)
