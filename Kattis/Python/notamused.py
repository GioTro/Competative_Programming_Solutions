# Problem : https://open.kattis.com/problems/notamused
import sys


def price(name, minutes):
    res = 0.0
    for _ in range(minutes):
        res += 0.1
    res = "{0:.2f}".format(res)
    return '{} ${}'.format(name, res)


days, dic = 0, {}
for line in sys.stdin:
    s = list(str(line).split())
    if s[0] == 'OPEN':
        days += 1
        continue
    if s[0] == 'CLOSE':
        print('Day %d' % days)
        for i in sorted(dic.keys()):
            print(price(i, dic[i]))
        dic = {}
        print('\n')
        continue

    if s[0] == 'ENTER':
        if s[1] not in dic.keys():
            dic.update({s[1]: 0})
        dic[s[1]] -= int(s[2])

    if s[0] == 'EXIT':
        dic[s[1]] += int(s[2])
