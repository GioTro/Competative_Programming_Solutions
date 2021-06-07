# Problem : https://open.kattis.com/problems/polymul1
def solve(p1, p2):
    deg = (len(p1) - 1) + (len(p2) - 1)
    res = [0 for _ in range(deg + 1)]

    i = (len(p1) - 1)
    for n1 in p1:
        j = len(p2) - 1
        for n2 in p2:
            res[i + j] += n1 * n2
            j -= 1
        i -= 1
    return res


cases = int(raw_input())
for i in range(cases):
    pol = []
    for j in range(2):
        _ = int(input())
        l = list(map(int, raw_input().split()))
        pol.append(l)
    res = solve(pol[0], pol[1])
    s = ""
    res = res[::-1]
    for f in res:
        s += str(f) + " "
    print((len(pol[0]) - 1) + (len(pol[1]) - 1))
    print(s.strip())
