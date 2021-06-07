# Solution to kattis problem source: https://open.kattis.com/problems/veci

import itertools

source = input()
integer = list(str(source))
compare = list(itertools.permutations(integer))
check = []
# Constructs an integer from the permutations of the source integer and
# appends it to "check" if that permutation is larger than source.
for i in range(len(compare)):
    string = ""
    for j in range(len(compare[i])):
        string += compare[i][j]
        if int(string) > source:
            check.append(int(string))
# if lenght of check there are no permutations larger than source, else
# print the integer with the smallest value in check.
if len(check) == 0:
    print(0)
else:
    print(sorted(check)[0])
