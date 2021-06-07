def solve(n):
    return (max(n) - min(n)) * 2


r = int(raw_input())

for i in range(r):
    throw = int(raw_input())
    print(solve(list(map(int, raw_input().split()))))
