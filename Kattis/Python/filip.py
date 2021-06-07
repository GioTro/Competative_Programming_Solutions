# Solution to kattis problem source: https://open.kattis.com/problems/filip

# handles input
number1, number2 = (map(int, raw_input().split()))
# flips the number
string1, string2 = str(number1), str(number2)
string1, string2 = string1[::-1], string2[::-1]
number1, number2 = int(string1), int(string2)

if number1 > number2:
    print number1
else:
    print number2
