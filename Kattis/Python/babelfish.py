import sys

dic = {}

line = raw_input()
while line != '':
    p, q = map(str, line.split())
    dic.update({q: p})
    line = raw_input()

for line in sys.stdin.readlines():
    if line[:-1] in dic:
        print(dic[str(line[:-1])])
    else:
        print('eh')
