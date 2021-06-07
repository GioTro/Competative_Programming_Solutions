# Problem : https://open.kattis.com/problems/owlandfox

def sumdig(n):
    s = str(n)
    res = 0
    for i in range(len(s)):
        res += int(s[i])
    return res


for i in range(int(raw_input())):
    n = int(raw_input())
    ns = sumdig(n) - 1
    if ns == 0:
        print("0")
        continue
    for i in range(n - 1, 0, -1):
        if sumdig(i) == ns:
            print(i)
            break
