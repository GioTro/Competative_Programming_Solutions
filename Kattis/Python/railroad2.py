def solve():
    _, y = map(int, input().split())
    return 'possible' if not (y % 2) else 'impossible'


print(solve())
