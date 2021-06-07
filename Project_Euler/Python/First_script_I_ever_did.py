# Find the sum of all the multiples of 3 or 5 below 1000
# This is the first computer programming I ever did... on 20th August 2017
# programming history being made!
# After a week of programming I realized you could just solve it like:
#  print(sum(list(i for i in range(1, target) if i%3==0 or i%5==0)))


a = 0
b = 0
c = 0
t1 = 334 * [0]

while a < 998:
    a += 3
    b += 1
    t1[b] = a


d = 0
e = 0
f = 0

t2 = 200 * [0]

while d < 995:
    d += 5
    e += 1
    t2[e] = d


t3 = t1 + t2

g = 0
x = 0

while g < 199:
    g += 1
    if t2[g] % 3 == 0:
        x += t2[g]

z = sum(t3) - x

print(z)
