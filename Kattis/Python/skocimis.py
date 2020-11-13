d = list(map(int, raw_input().split()))
print(max(d[2] - d[1] - 1, max(d[1] - d[0] - 1, 0)))