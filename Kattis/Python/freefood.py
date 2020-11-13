import sys
# One line chop
print(len(set([j for i in [list(map(int, line.split())) for line in list(sys.stdin)[1:]] for j in range(i[0], i[1] + 1)])))