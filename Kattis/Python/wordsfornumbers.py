# Problem : https://open.kattis.com/problems/wordsfornumbers
import sys
import re

word = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'}


def convert(n):
    if len(n) == 1:
        return word[n]
    elif int(n[1]) == 0:
        return word[int(str(n[0]) + '0')]
    else:
        return word[int(str(n[0]) + '0')] + '-' + word[int(n[1])]


for line in sys.stdin:
    res = re.findall('[0-9]+', str(line))
    r = []
    for i in res:
        r.append(convert(i))

    res2 = list(map(str, line.split()))
    if len(res2) > 0:
        if res2[0] in res:
            r[0] = r[0][0].upper() + r[0][1:]
    s = ''
    for i in res2:
        if i in res:
            s += r[0] + ' '
            r = r[1:]
        else:
            s += i + ' '
    print(s.strip())
