# Solution for kattis problem source: https://open.kattis.com/problems/judgingmoose

integers = list(map(int, raw_input().split()))
if integers[0] == 0 and integers[1] == 0:
    print("Not a moose")
else:
    if integers[0] != integers[1]:
        if integers[0] > integers[1]:
            print("Odd %s" % (integers[0] * 2))
        else:
            print("Odd %s" % (integers[1] * 2))
    if integers[0] == integers[1]:
        if integers[0] >= integers[1]:
            print("Even %s" % (integers[0] * 2))
        else:
            print("Even %s" % (integers[1] * 2))
