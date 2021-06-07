# Solution for kattis problem source :
# https://open.kattis.com/problems/permutedarithmeticsequence

def arithmetic(n):
    d = n[1] - n[0]
    for i in range(1, len(n) - 1):
        if n[i + 1] - n[i] != d:
            return False
        return True


def checkSeries(lista):
    control = lista[1:]
    if arithmetic(control):
        print("arithmetic")
    elif arithmetic(sorted(control)):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")


limit = input()
series = []
for i in range(limit):
    series.append(list(map(int, raw_input().split())))

for i in range(len(series)):
    checkSeries(series[i])
