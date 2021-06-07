# Solution to kattis problem source: https://open.kattis.com/problems/pet


# HandleInput
contestant = []
for i in range(0, 5):
    contestant.append(sum(map(int, raw_input().split())))

winner = 0
index = 0
for i in range(0, len(contestant)):
    if contestant[i] > winner:
        winner = contestant[i]
        index = i + 1

print index, winner
