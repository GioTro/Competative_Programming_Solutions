# Problem : https://open.kattis.com/problems/asciiaddition
# This version is a derivative from the original source
# Minor changes has to be made for it to pass kattis as it to slow @constructing
# Bored to revert back

def chop(l):
    index, res = 0, []
    while True:
        s = ''
        for i in l:
            s += i[index:index + 5]
        index += 6
        res.append(s)
        if (index > len(l[0])):
            break
    return res


def construct(s):
    numbp = {q: p for p, q in numb.items()}
    res = []
    for i in s:
        res.append(numbp[int(i)])

    s, index, ret = '', 0, ['' for _ in range(len(s))]
    for i in res:
        j = 0
        while j < 7:
            ret[j] += res[index][:5] + '.'
            res[index] = res[index][5:]
            j += 1
        index += 1

    return ret


p = [str(input()) for _ in range(7)]
p = chop(p)
numb = {
    '....x....x....x....x....x....x....x': 1,
    'xxxxx....x....xxxxxxx....x....xxxxx': 2,
    'xxxxx....x....xxxxxx....x....xxxxxx': 3,
    'x...xx...xx...xxxxxx....x....x....x': 4,
    'xxxxxx....x....xxxxx....x....xxxxxx': 5,
    'xxxxxx....x....xxxxxx...xx...xxxxxx': 6,
    'xxxxx....x....x....x....x....x....x': 7,
    '.......x....x..xxxxx..x....x.......': '+',
    'xxxxxx...xx...xxxxxxx...xx...xxxxxx': 8,
    'xxxxxx...xx...xxxxxx....x....xxxxxx': 9,
    'xxxxxx...xx...xx...xx...xx...xxxxxx': 0}

s, res = '', []
for i in p:
    t = numb[i]
    if t == '+':
        res.append(int(s))
        s = ''
    else:
        s += str(t)
res.append(int(s))
p = construct(str(sum(res)))
for i in p:
    print(i[:-1])
