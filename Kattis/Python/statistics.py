import sys

case = 0
for line in sys.stdin:
    case += 1
    data = list(map(int, line.split()))[1:]
    print(
        'Case %d: %d %d %d' %
        (case,
         min(data),
         max(data),
         max(data) -
         min(data)))
