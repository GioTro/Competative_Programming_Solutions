def summa(s):
    res = 0
    for char in s:
        res += (ord(char) - 65)
    return res


def rot(s, n):
    r = ""
    for i in range(len(s)):
        r += chr(((ord(s[i]) - 65) + n) % 26 + 65)
    return r


def solve(s):
    t = len(s) / 2
    t1, t2 = s[:t], s[t:]
    t1 = rot(t1, summa(t1))
    t2 = rot(t2, summa(t2))

    r = ""
    for i in range(len(t1)):
        r += rot(t1[i], ord(t2[i]) - 65)
    return r


print(solve(str(raw_input())))
