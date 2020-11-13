# Problem : https://open.kattis.com/submissions/4013135
def read(l, n):
    r = []
    for i in range(len(l[0])):
        s = ""
        for j in range(len(l)):
            s += l[j][i]
        r.append(s)
    rp = [i.lower() for i in r]
    return solve(r, sorted(rp), n)

def construct(l, toReturn):
    for i in range(len(toReturn)):
        toReturn[i] += l[i]
        
def solve(toPrint, order, n):
    toReturn = ["" for _ in range(n)]
    for s in order:
        for l in toPrint:
            if l.lower() == s:
                construct(l, toReturn)
                toPrint.remove(l)
                break
    return toReturn

s = ""
while True:
    p, q = map(int, input().split())
    if p == 0 and q == 0:
        break
    l = [str(input()) for _ in range(p)]
    r = read(l, p)
    for i in r:
        s += i+"\n"
    s += "\n"

print(s.strip())
