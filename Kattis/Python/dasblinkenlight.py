def solve(p, q, s):
    pl = [p]
    ql = [q]
    while (pl[-1] <= s or ql[-1] <= s):
        if pl[-1] <= s:
            pl.append(pl[-1] + pl[0])
        if ql[-1] <= s:
            ql.append(ql[-1] + ql[0])
    pl = pl[:-1]
    ql = ql[:-1]

    for i in pl:
        if i in ql:
            return "yes"

    return "no"


p, q, s = map(int, raw_input().split())
print(solve(p, q, s))
