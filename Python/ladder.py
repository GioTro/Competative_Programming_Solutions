# Solution to kattis problem source: https://open.kattis.com/problems/ladder

import math


def function(height, angle):
    radians = math.radians(angle)
    length = height / (math.sin(radians))
    length = int(math.ceil(length))
    return length


height, angle = map(int, raw_input().split())
print(function(height, angle))
