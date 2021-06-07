r = int(raw_input())

for i in range(r):
    s = str(raw_input())
    if "=" in s:
        print("skipped")
    else:
        p, q = map(int, s.split('+'))
        print(p + q)
