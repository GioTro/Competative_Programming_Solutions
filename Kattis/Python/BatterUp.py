# Solution for Kattis problem: https://open.kattis.com/problems/batterup

s = int(input())
t = list(input().split())
score = 0

for i in t:
    if int(i) == -1:
        s += int(i)
    else:
        score += int(i)

print(float(score / s))
