# Solution to kattis problem source: https://open.kattis.com/problems/oddities

def handleOutput(myList):
    for i in range(0, len(myList)):
        if myList[i] % 2 == 0:
            print("%s is even" % (myList[i]))
        else:
            print("%s is odd" % (myList[i]))


# Handle input
integers = []
index = int(input())
for i in range(0, index):
    integers.append(int(input()))

handleOutput(integers)
