# Problem : https://open.kattis.com/problems/calculatingdartscores
def solve(n):
    def check(n): return True if not 0 < n <= 180 else False
    if check(n):
        return 'impossible'

    def ev(n): return sum([i[0] * i[1] for i in n])

    def succ(): for a in range(1, 4):
        for b in range(0, 4):
            for c in range(0, 4):
                for i in range(1, 21):
                    for j in range(1, 21):
                        for k in range(1, 21):
                            yield [[a, i], [b, j], [c, k]]
    for i in succ():
        if ev(i) == n:
            return i
    return 'impossible'


def p(l):
    dic = {1: 'single', 2: 'double', 3: 'triple'}
    if l == 'impossible':
        print(l)
    else:
        for i in l:
            if i[0] == 0:
                continue
            else:
                print(dic[i[0]] + ' ' + str(i[1]))


p(solve(int(input())))
