import sys
import re


def solve(matrix, n):
    occurance = []
    for row in matrix:
        occurance.append(len(re.findall('\\*', row)))
    res = []
    t = 0
    for i in occurance:
        s = ""
        for j in range(t):
            s += '.'

        for j in range(i):
            s += '*'
            t += 1

        for j in range((n - len(s))):
            s += '.'
        res.append(s[::-1])

    return res


matrix, boo = [], True
for line in sys.stdin:
    if str(line) == '\n':
        if boo:
            boo = False
        else:
            print()

        res = solve(matrix, len(matrix[0]))
        for i in res:
            print(i)
        matrix = []
        continue
    else:
        matrix.append(str(line))
