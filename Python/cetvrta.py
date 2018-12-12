#Solution for kattis problem source: https://open.kattis.com/problems/cetvrta

coordinates = []
x = []
y = []

for i in range(0, 3):
    coordinates.append(list(input().split(" ")))

for i in range(0, 3):
    x.append(coordinates[i][0])
    y.append(coordinates[i][1])

coordinates = [0, 0]

for i in range(0, 3):
    if x.count(x[i]) == 1:
        coordinates[0] = x[i]
    if y.count(y[i]) == 1:
        coordinates[1] = y[i]

print("%s %s" % (coordinates[0], coordinates[1]))
