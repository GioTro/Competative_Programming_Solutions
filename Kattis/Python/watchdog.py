# Problem : https://open.kattis.com/problems/watchdog
# Exhaustive linear search.
# Solution should be redefined to output the first valid solution.
# That is if a solution [x1, y1] is found then you don't have to look for
# solutions [x2 > x1, y2]
def successor(k, h):
    if k[0] + 1 > h:
        k[0], k[1] = 0, k[1] + 1
    else:
        k[0] += 1
    return k


def check(points, k, l):
    for i in points:
        if (((i[0] - k[0])**2 + (i[1] - k[1])**2) > l**2):
            return False
        else:
            continue
    return True

# Find longest possible leash for a given point relative to height


def leash(h, k):
    t = [k[0], h - k[0], k[1], h - k[1]]
    return min(t)


def solve(h, points, k, solutions):
    solutions = []
    while k != [h, h]:
        l = leash(h, k)
        if check(points, k, l):
            solutions.append(list(k))
        k = successor(k, h)
    return solutions


def resolve(l):
    x, y = 1337**3, 1337**3
    for i in l:
        x = min(x, i[0])

    for i in l:
        if i[0] == x:
            y = min(y, i[1])
    return [x, y]


limit = int(input())
for i in range(limit):
    h, c = map(int, input().split())
    points = []
    for j in range(c):
        x, y = map(int, input().split())
        points.append([x, y])

    answer = solve(h, points, [0, 0], [])
    for i in points:
        if i in answer:
            answer.remove(i)
    if len(answer) == 0:
        print('poodle')
    else:
        answer = resolve(answer)
        print("%d %d" % (answer[0], answer[1]))
