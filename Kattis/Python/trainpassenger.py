# ugly solution for kattis problem source:
# https://open.kattis.com/problems/trainpassengers

data = list(map(int, raw_input().split()))
Capacity = data[0]
iterate = data[1]
data = []

for i in range(0, iterate):
    hold = list(map(int, raw_input().split()))
    data.append(hold)

dontPrint = True
# Do the calculation
# special cases
if data[0][0] > 0 or data[-1][2] > 0 or data[-1][1] > 0:
    print("impossible")
    dontPrint = False

# if data[-1][1]>0:
#    print("impossible")
#    dontPrint = False

# first case
passengers = data[0][1]
if passengers > Capacity:
    print("impossible")
    dontPrint = False
if passengers < Capacity and data[0][2] > 0:
    print("impossible")
    dontPrint = False
# all remaining cases except last
if dontPrint:
    for i in range(1, len(data) - 1):
        passengers -= data[i][0]
        if passengers < 0:
            print("impossible")
            dontPrint = False
            break
        passengers += data[i][1]
        if passengers > Capacity:
            print("impossible")
            dontPrint = False
            break
        if passengers < Capacity and data[i][2] > 0:
            print("impossible")
            dontPrint = False
            break

# EmptyTrain
passengers -= data[-1][0]

# if not empty impossible
if dontPrint and passengers != 0:
    print("impossible")
    dontPrint = False

if dontPrint:
    print("possible")
