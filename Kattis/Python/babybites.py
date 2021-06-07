# Problem : https://open.kattis.com/problems/babybites

r = int(raw_input())
d = list(map(str, raw_input().split()))
t = True
for i in range(r):
    if not (d[i] == str(i + 1) or d[i] == 'mumble'):
        print('something is fishy')
        t = False
        break

if t:
    print('makes sense')
