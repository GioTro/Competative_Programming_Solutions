def solve(s, n):
    res = ""
    for i in range(len(s)):
        if s[i] == '_':
            t = (26 + n) % 28
        elif s[i] == '.':
            t = (27 + n) % 28
        else:
            t = (ord(s[i]) - 65 + n) % 28

        if t == 26:
            res += '_'
        elif t == 27:
            res += '.'
        else:
            res += str(unichr(t + 65))

    return res


while (True):
    d = list(map(str, raw_input().split()))

    if int(d[0]) == 0:
        break
    else:
        print(solve(d[1][::-1], int(d[0])))
