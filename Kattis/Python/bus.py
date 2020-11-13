# Problem : https://open.kattis.com/problems/bus
for _ in range(int(input())):
    res = 0
    for i in range(int(input())):
        res += 0.5
        res *= 2
    print(int(res))
