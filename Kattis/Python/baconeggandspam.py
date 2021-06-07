# Problem : https://open.kattis.com/problems/baconeggsandspam
def solve(l):
    names = []
    ingredients = []
    for i in l:
        names.append(i[0])
        for j in i[1]:
            ingredients.append(j)
    ingredients = list(set(ingredients))
    out(names, sorted(ingredients), l)


def out(n, ing, l):
    for i in ing:
        s = str(i)
        names = []
        for j in l:
            if i in j[1]:
                names.append(j[0])
        names = sorted(names)
        for na in names:
            s += " {}".format(na)
        print(s)
    print("")


r = int(raw_input())
while (r != 0):
    res = []
    for i in range(r):
        d = list(map(str, raw_input().split()))
        t = [d[0]]
        l = []
        for j in range(1, len(d)):
            l.append(d[j])
        t.append(l)
        res.append(t)
    solve(res)
    r = int(raw_input())
