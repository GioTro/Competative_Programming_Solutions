r = int(raw_input())
seen = []

for i in range(r):
    d = list(map(str, raw_input().split()))
    if d[0] not in seen:
        seen.append(d[0])
        print("{} {}".format(d[0], d[1]))
        if len(seen) >= 12:
            break
    else:
        continue
