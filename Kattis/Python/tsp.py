# Problem : https://open.kattis.com/problems/tsp
def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def solve(tour, used, points, n):
    for i in range(1, n):
        best = -1
        for j in range(0, n):
            t = points[tour[i - 1]]
            if not used[j] and (
                best == -
                1 or dist(
                    t,
                    points[j]) < dist(
                    t,
                    points[best])):
                best = j
        tour.append(best)
        used[best] = True
    return tour


p, q = int(input()), []
for i in range(p):
    x, y = map(float, input().split())
    q.append((x, y))

tour = [0]
used = [True] + [False for _ in range(p - 1)]
tour = solve(tour, used, q, p)

for i in tour:
    print(i)
