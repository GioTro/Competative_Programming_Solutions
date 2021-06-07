r = int(raw_input())
t = "Simon says"
for i in range(r):
    s = str(raw_input())

    if (s[:len(t)] == t):
        print(s[len(t):])
