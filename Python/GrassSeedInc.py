#Solution for kattis problem: https://open.kattis.com/problems/grassseed

cost = float(input())
n_lawn = int(input())
l = []

for i in range(0, n_lawn):
    l.append(list(input().split()))

p = []

for i in l:
    prod = 1
    for j in i:
        prod *= float(j)
    p.append(prod*cost)

print(sum(p))




