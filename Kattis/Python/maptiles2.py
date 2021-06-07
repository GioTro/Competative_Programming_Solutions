quadkey = str(input())
x = y = ''

for c in quadkey:
    x += '0' if c == '0' or c == '2' else '1'
    y += '0' if c == '0' or c == '1' else '1'

print('%d %d %d' % (len(quadkey), int(x, base=2), int(y, base=2)))
