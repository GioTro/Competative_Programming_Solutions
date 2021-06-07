# Problem : https://open.kattis.com/problems/quickbrownfox
def solve(s, chars):
    for i in s:
        if i in chars:
            chars.remove(i)
    return chars


chars = [chr(i) for i in range(97, 97 + 26)]
p = int(raw_input())
for _ in range(p):
    line = str(raw_input()).lower()
    s = solve(line, list(chars))
    if len(s) == 0:
        print('pangram')
    else:
        print "missing " + "".join(sorted(s))
