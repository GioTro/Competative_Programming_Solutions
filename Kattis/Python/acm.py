import sys

score = 0
count = 0
array = [0 for i in range(25)]

for line in sys.stdin:
    inp = line.split()

    if len(inp) == 1:
        break
    else:
        t, p, a = inp

    if a == 'wrong':
        array[ord(p) - ord('A')] += 20
    else:
        count += 1
        score += int(t) + array[ord(p) - ord('A')]

print('%d %d' % (count, score))
