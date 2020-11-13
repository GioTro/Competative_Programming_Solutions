#Problem 6 as a for loop.

SquareSum = 0

for i in range(1, 100+1):
    SquareSum += i**2

SumInt = 0

test = sum(list(i for i in range(1,100+1)))**2

print(test)

for i in range(1, 100+1):
    SumInt += i

result = (SumInt**2) - SquareSum

print("Result: %s" % (result))
