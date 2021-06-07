# Solution to kattis problem source:
# https://open.kattis.com/problems/plantingtrees
import time


# HandleInput
#limit = int(input())
#seeds = list(map(int, raw_input().split()))
#seeds = sorted(seeds, reverse = True)
count = 0

seeds = []
for i in range(0, 100000):
    seeds.append(i)

start = time.time()
# Performs the calculation
for i in range(0, len(seeds)):
    seeds[i] = seeds[i] + count + 1
    count += 1

# find highest value
maxValue = 0
for i in range(0, len(seeds)):
    if seeds[i] > maxValue:
        maxValue = seeds[i]

print(maxValue + 1)

elapsed = time.time() - start
