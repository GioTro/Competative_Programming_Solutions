# Ugly solution for :: https://open.kattis.com/problems/2048

def solve(m, d):
    if d == 0:
        for j in range(4):
            f, c = set(), 1
            while c:
                c = 0
                for i in range(1, 4):
                    if m[j][i] == 0:
                        continue
                    if m[j][i - 1] == 0:
                        m[j][i - 1] = m[j][i]
                        m[j][i] = 0
                        c += 1
                        if i in f:
                            f.remove(i)
                            f.add(i - 1)
                    elif i not in f and (i - 1) not in f and m[j][i - 1] == m[j][i]:
                        m[j][i - 1] *= 2
                        m[j][i] = 0
                        f.add(i - 1)
                        c += 1
    if d == 1:
        for i in range(4):
            f, c = set(), 1
            while c:
                c = 0
                for j in range(1, 4):
                    if m[j][i] == 0:
                        continue
                    if m[j - 1][i] == 0:
                        m[j - 1][i] = m[j][i]
                        m[j][i] = 0
                        c += 1
                        if j in f:
                            f.remove(j)
                            f.add(j - 1)
                    elif j not in f and (j - 1) not in f and m[j - 1][i] == m[j][i]:
                        m[j - 1][i] *= 2
                        m[j][i] = 0
                        f.add(j - 1)
                        c += 1
    if d == 2:
        for j in range(4):
            f, c = set(), 1
            while c:
                c = 0
                for i in range(2, -1, -1):
                    if m[j][i] == 0:
                        continue
                    if m[j][i + 1] == 0:
                        m[j][i + 1] = m[j][i]
                        m[j][i] = 0
                        c += 1
                        if i in f:
                            f.remove(i)
                            f.add(i + 1)
                    elif i not in f and (i + 1) not in f and m[j][i + 1] == m[j][i]:
                        m[j][i + 1] *= 2
                        m[j][i] = 0
                        f.add(i + 1)
                        c += 1
    if d == 3:
        for i in range(4):
            f, c = set(), 1
            while c:
                c = 0
                for j in range(2, -1, -1):
                    if m[j][i] == 0:
                        continue
                    if m[j + 1][i] == 0:
                        m[j + 1][i] = m[j][i]
                        m[j][i] = 0
                        c += 1
                        if j in f:
                            f.remove(j)
                            f.add(j + 1)
                    elif j not in f and (j + 1) not in f and m[j + 1][i] == m[j][i]:
                        m[j + 1][i] *= 2
                        m[j][i] = 0
                        f.add(j + 1)
                        c += 1
    return m


def p(m):
    for i in range(4):
        print("{} {} {} {}".format(m[i][0], m[i][1], m[i][2], m[i][3]))


m = [list(map(int, raw_input().split())) for _ in range(4)]
p(solve(m, int(raw_input())))
