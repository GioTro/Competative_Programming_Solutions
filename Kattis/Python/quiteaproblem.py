# Problem : https://open.kattis.com/problems/quiteaproblem
import sys, re

for line in sys.stdin:
    d = str(line).lower()
    x = re.findall('problem', d)
    if len(x) > 0:
        print('yes')
    else:
        print('no')
