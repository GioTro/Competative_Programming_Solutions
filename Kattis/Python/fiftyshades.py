import sys

f = lambda s : True if ('pink' in s or 'rose' in s) else False
i = sum([f(line.lower()) for line in sys.stdin])
print(i if i != 0 else 'I must watch Star Wars with my daughter')