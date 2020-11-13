input()
inp = list(map(int, input().split()))
inp = sorted(inp)[::-1]
a = [inp[i] for i in range(0, len(inp), 2)]
b = [inp[i] for i in range(1, len(inp), 2)]

print('%d %d' % (sum(a), sum(b)))

