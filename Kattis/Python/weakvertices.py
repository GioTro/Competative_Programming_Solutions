# Solution to weakvertices
import sys


def solve(adj_matrix):
    toReturn = []
    n = len(adj_matrix)

    for i in range(n):
        weak = True  # Assume true
        for j in range(n):
            for k in range(n):
                if i == j == k:
                    pass
                else:
                    if (adj_matrix[i][k] == adj_matrix[i]
                            [j] == adj_matrix[j][k] == 1):
                        weak = False
        toReturn.append(weak)

    return toReturn


inpt = [line for line in sys.stdin]

while len(inpt) > 1:
    num = int(inpt.pop(0))
    adj_matrix = []

    for i in range(num):
        adj_matrix.append([int(j) for j in inpt.pop(0).split()])

    answer = solve(adj_matrix)
    toPrint = ''
    for i in range(len(answer)):
        if answer[i]:
            toPrint += str(i) + ' '
    print(toPrint.strip())
