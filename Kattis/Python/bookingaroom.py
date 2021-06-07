# Solution to kattis problem source:
# https://open.kattis.com/problems/bookingaroom

rooms = list(map(int, raw_input().split()))

nRooms = rooms[0]
nBooked = rooms[1]

rooms = []
for i in range(0, nBooked):
    rooms.append(int(input()))

if nBooked == nRooms:
    print("too late")
else:
    for i in range(1, nRooms + 1):
        if i not in rooms:
            print i
            break
