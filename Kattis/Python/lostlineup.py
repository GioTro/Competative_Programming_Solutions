import sys

inp = [list(map(int, i.split())) for i in sys.stdin]
inp = inp[1]
string = '1 '
dic = {}

for i in range(len(inp)):
	dic[inp[i]] = i + 2

for i in range(len(inp)):
	string += str(dic[i]) + ' '

print(string)