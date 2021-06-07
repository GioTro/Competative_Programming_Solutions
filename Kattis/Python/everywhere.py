# Solution for kattis problem source:
# https://open.kattis.com/problems/everywhere

def setter(integer):
    mySet = set()
    for i in range(0, integer):
        mySet.add(str(input()))
    return len(mySet)


limit = int(input())
nCities = []
for i in range(0, limit):
    nCities.append(setter(int(input())))

for i in range(0, limit):
    print(nCities[i])
