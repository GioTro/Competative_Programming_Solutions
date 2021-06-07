import re


def solve(key, string):
    res = [len(re.findall('(?={})'.format(key), string)), 0, 0]
    keyp, keyp2 = [], []

    # Type 2
    for i in range(len(key)):
        keyp.append(key[:i] + key[i + 1:])
        for j in ['A', 'C', 'G', 'T']:
            keyp2.append(key[:i] + j + key[i:])
    for j in ['A', 'C', 'G', 'T']:
        keyp2.append(key + j)
    # Type 2
    for i in set(keyp):
        res[1] += len(re.findall('(?={})'.format(i), string))

    # Type 3
    for i in set(keyp2):
        res[2] += len(re.findall('(?={})'.format(i), string))
    return res


while True:
    s = str(input())
    if s == '0':
        break
    else:
        key, string = map(str, s.split())
        res = solve(key, string)
        print("{} {} {}".format(res[0], res[1], res[2]))
