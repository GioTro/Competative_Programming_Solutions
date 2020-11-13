# Problem : https://open.kattis.com/problems/towering
# Solves the problem by taking all possible differences between the total height of a tower and one of the blocks
# and matches that with all possible sums we can create using two of the blocks.

def findDifference(d, h):
    return {h-i:[h, i] for i in d}

def sumOfTwo(d):
    ret = {}
    while len(d) > 0:
        t = d[0]
        d = d[1:]
        for i in d:
            ret.update({t+i:[t, i]})
    return ret

# Resolves collisions by finding the set consisting of only unique numbers
def resolve(t1, t2):
    for i in t1:
        for j in t2:
            if len(set(i+j)) == 6:
                return [i, j]

d = list(map(int, input().split()))
h1, h2 = d[-2], d[-1]
d = d[:-2]
d1 = findDifference(d, h1)
d2 = findDifference(d, h2)
s = sumOfTwo(d)

# Find candidate combinations
tower1 = []
for i in d1.keys():
    for j in s.keys():
        if j == i:
            tower1.append(s[j]+[d1[i][1]])

tower2 = []
for i in d2.keys():
    for j in s.keys():
        if j == i:
            tower2.append(s[j]+[d2[i][1]])

r = resolve(tower1, tower2)
tower1 = sorted(r[0])[::-1]
tower2 = sorted(r[1])[::-1]
print("%d %d %d %d %d %d" % (tower1[0], tower1[1], tower1[2], tower2[0], tower2[1], tower2[2]))
            
