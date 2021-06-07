# Problem : https://open.kattis.com/problems/epigdanceoff
def solve(l):
    res = 0
    for i in range(len(l[0])):
        b = True
        for j in l:
            if j[i] == '$':
                b = False
        if b:
            res += 1
    return res


p, q = map(int, input().split())
d = [str(input()) for _ in range(p)]
print(solve(d) + 1)
