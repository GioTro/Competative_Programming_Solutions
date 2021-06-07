# Solution for kattis problem source: https://open.kattis.com/problems/kornislav
# I solved a few scenarios on paper and found that it follows the pattern::
# smallest times the second largest. Playing around with it on paper made
# it obvious how it works.

integers = sorted(list(map(int, raw_input().split())))
solution = integers[0] * integers[2]
print solution
