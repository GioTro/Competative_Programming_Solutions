#Ugly solution for kattis problem source: https://open.kattis.com/problems/sevenwonders

MainString = str(raw_input())

T, C, G = 0, 0, 0
for i in range(0, len(MainString)):
    if MainString[i] == "T":
        T += 1
    if MainString[i] == "G":
        G += 1
    if MainString[i] == "C":
        C += 1

total = T**2 + C**2 + G**2
minimum = G
if T<minimum:
    minimum = T
if C < minimum:
    minimum = C

total += minimum*7

print(total)
