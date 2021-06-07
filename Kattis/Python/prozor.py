# Problem : https://open.kattis.com/problems/prozor
# Messy and slow, should be redefined with a dictionairy or something.
def read(window):
    flies = []
    for i in range(len(window)):
        for j in range(len(window[0])):
            if window[i][j] == '*':
                flies.append([i, j])
    return flies


def solve(flies, racket, p, q):
    killCount, anchor = 0, [0, 0]
    for i in range(0, p - racket + 1):
        for j in range(0, q - racket + 1):
            killz = 0
            for f in flies:
                if f[0] > i and f[0] < (i + racket - 1):
                    if f[1] > j and f[1] < (j + racket - 1):
                        killz += 1
            if killz > killCount:
                killCount = killz
                anchor = [i, j]
    return [anchor, killCount]


def findPipes(anchor, racket):
    corners = [anchor, [anchor[0], anchor[1] + racket], [anchor[0] + \
        racket, anchor[1]], [anchor[0] + racket, anchor[1] + racket]]

    bars = [[corners[0][0],
             i] for i in range(corners[0][1] + 1,
                               corners[0][1] + racket)] + [[corners[0][0] + racket,
                                                            i] for i in range(corners[0][1] + 1,
                                                                              corners[0][1] + racket)]

    pipes = [[i,
              corners[0][1]] for i in range(corners[0][0] + 1,
                                            corners[0][0] + racket)] + [[i,
                                                                         corners[0][1] + racket] for i in range(corners[0][0] + 1,
                                                                                                                corners[0][0] + racket)]

    return [corners, bars, pipes]


def prettyPrint(anchor, flies, racket, kc, p, q):
    window = []
    t = findPipes(anchor, racket - 1)
    corners, bars, pipes = t[0], t[1], t[2]
    for i in range(p):
        row = ''
        for j in range(q):
            cc = [i, j]
            if [i, j] in corners:
                row += '+'
            elif [i, j] in bars:
                row += '-'
            elif [i, j] in pipes:
                row += '|'
            elif [i, j] in flies:
                row += '*'
            else:
                row += '.'

        window.append(row)
    print(kc)
    for i in window:
        print(i)


p, q, r = map(int, input().split())
window = []

for i in range(p):
    window.append(str(input()))
flies = read(window)
t = solve(flies, r, p, q)
prettyPrint(t[0], flies, r, t[1], p, q)
