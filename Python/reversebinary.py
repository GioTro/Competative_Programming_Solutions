# Solution to kattis problem source: https://open.kattis.com/problems/reversebinary

# def function(n):
#    theString = str(n)
#    myNumber = 0
#    for i in range(1, len(theString)+1):
#        myNumber += count(int(theString[-i]), i-1)
#    return myNumber
#
# def count(x, y):
#    if x == 1:
#        myNumber = 2**y
#    else:
#        myNumber = 0
#    return int(myNumber)
#
# myNumber = int(input())
# binary = bin(myNumber)
# binString = str(binary)
# binString = binString[:1:-1]
# reversedBinary = str(binString)
# myNumber = int(reversedBinary)
# Don't know how to parse str --> binary
# print(function(myNumber))
# it worked!

# oneliner:
integer = print(int(bin(input())[:1:-1], base=2))
# lol
