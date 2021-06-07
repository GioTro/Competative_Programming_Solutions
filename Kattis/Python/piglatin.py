# Problem : https://open.kattis.com/problems/piglatin
import sys


def construct(w):
    s = ""
    for c in w:
        if c not in ['a', 'e', 'i', 'o', 'u', 'y']:
            s += c
        else:
            break
    return w[len(s):] + s


for line in sys.stdin:
    s, r = list(map(str, line.split())), []
    for w in s:
        if w[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
            r.append(w + 'yay')
        else:
            r.append(construct(w) + 'ay')
    print(" ".join(r).strip())
