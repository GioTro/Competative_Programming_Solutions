import sys
inp = [list(line.strip()) for line in sys.stdin]
inp = inp[1:]


def getCols(array):
    return [[array[i][j] for i in range(len(array))]
            for j in range(len(array))]


rows = [''.join(row) for row in inp]
cols = [''.join(row) for row in getCols(inp)]

boolean = 1

for row in rows:
    if ('BBB' or 'WWW') in row:
        boolean = 0
        break

    count = 0
    for c in row:
        if c == 'W':
            count += 1
        else:
            count -= 1

    if count != 0:
        boolean = 0
        break

if boolean:
    for col in cols:
        if ('BBB' or 'WWW') in col:
            boolean = 0
            break

        count = 0

        for c in col:
            if c == 'W':
                count += 1
            else:
                count -= 1

        if count != 0:
            boolean = 0
            break
print(boolean)
