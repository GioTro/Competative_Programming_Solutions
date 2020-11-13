# Problem : https://open.kattis.com/problems/delimitersoup
def push(l, e):
	l.append(e)

def pop(l):
	t = l[-1]
	l = l[:-1]
	return [t, l]

ceil = int(raw_input())
p = str(raw_input())
complement = {'(' : ')', '{' : '}', '[' : ']'}
stack, index = [], 0
for i in p:
	if i not in ['(', '{', '[', ')', ']', '}']:
		index += 1
		continue

	if i in ['(', '{', '[']:
		push(stack, i)
	else:
		if len(stack) == 0:
			print("{} {}".format(i, index))
			break
		else:
			e = pop(stack)		
			stack = e[1]
			if i != complement[e[0]]:
				print("{} {}".format(i, index))
				break
	index += 1

if index == ceil:
	print('ok so far')