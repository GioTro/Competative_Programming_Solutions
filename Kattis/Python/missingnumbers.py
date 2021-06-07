import sys

inp = [int(line) for line in sys.stdin]
inp = inp[1:]

if len(inp) == max(inp):
    print('good job')
else:
    array = [0 for i in range(max(inp))]
    for i in inp:
        array[i - 1] = 1

    for i in range(len(array)):
        if array[i] == 0:
            print(i + 1)
