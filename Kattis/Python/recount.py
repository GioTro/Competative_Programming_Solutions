# Problem : https://open.kattis.com/problems/recount
line, dic = '', {}
while line != '***':
	line = str(input())
	if line not in dic.keys():
		dic.update({line : 1})
	else:
		dic[line] += 1

l = list(dic.values())
if l.count(max(l)) > 1:
	print('Runoff!')
else:
	t = max(l)
	for i in dic.keys():
		if dic[i] == t:
			print(i)