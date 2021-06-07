# Problem : https://open.kattis.com/problems/4thought
# Some parts are a bit screwed up
def plus(p, q):
    return p + q


def minus(p, q):
    return p - q


def divide(p, q):
    return int(p / q)


def mult(p, q):
    return p * q


def st(res, t, index):
    l, j = [], 0
    while j < len(res):
        if j == index:
            l.append(t)
            j += 2
        else:
            l.append(res[j])
            j += 1
    return l


def eval(s):
    res, index, sp = [4, 4, 4, 4], 0, s.copy()
    while True:
        if len(s) == 0:
            break
        if s[index] == mult:
            res = st(res, mult(res[index], res[index + 1]), index)
            s.remove(mult)
            index = 0
            continue
        if s[index] == divide:
            res = st(res, divide(res[index], res[index + 1]), index)
            s.remove(divide)
            index = 0
            continue
        if mult in s or divide in s:
            index += 1
            continue
        else:
            if s[index] == plus:
                res = st(res, plus(res[index], res[index + 1]), index)
                s.remove(plus)
                index = 0
                continue
            if s[index] == minus:
                res = st(res, minus(res[index], res[index + 1]), index)
                s.remove(minus)
                index = 0
                continue
    s = sp
    return int(res[0])


def succ(s):
    if seq.index(s[0]) == 3:
        s[0] = plus
        if seq.index(s[1]) == 3:
            s[1] = plus
            s[2] = seq[seq.index(s[2]) + 1]
        else:
            s[1] = seq[seq.index(s[1]) + 1]
    else:
        s[0] = seq[seq.index(s[0]) + 1]
    return s


def req(n, sequence):
    t = sequence.copy()
    tp = eval(sequence)
    if t == [divide, divide, divide]:
        if tp == n:
            return t
        else:
            return []

    if (tp == n):
        return t
    else:
        return req(n, succ(t))


seq = [plus, minus, mult, divide]
dic = {plus: "+", minus: "-", mult: "*", divide: "/"}
bas = [plus, plus, plus]

r = int(input())
d = [int(input()) for _ in range(r)]

for i in d:
    s = req(i, bas.copy())
    if len(s) == 0:
        print("no solution")
    else:
        print("4 {} 4 {} 4 {} 4 = {}".format(
            dic[s[0]], dic[s[1]], dic[s[2]], i))
