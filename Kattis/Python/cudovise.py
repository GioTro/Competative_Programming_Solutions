# Solution cudoviste
import sys


def solve(x, y, grid):
    def square(x, y, grid): return grid[x][y] + \
        grid[x + 1][y] + grid[x][y + 1] + grid[x + 1][y + 1]
    count = {}
    for i in range(x - 1):
        for j in range(y - 1):
            s = square(i, j, grid)
            if '#' in s:
                continue
            else:
                # Count cars
                index = sum([c == 'X' for c in s])
                try:
                    count[index] += 1
                except BaseException:
                    count[index] = 1
    return count


def read():
    lst = [line for line in sys.stdin]
    x, y = lst[0].split()
    return (int(x), int(y), lst[1:])


x, y, grid = read()
dct = solve(x, y, grid)
for i in range(5):
    try:
        print(dct[i])
    except BaseException:
        print(0)
