import time

# Check if a number is pandigital


def panDigitial(number):
    c = str(number)
    check = []
    compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 9):
        check.append(int(c[i]))
    sort = sorted(check)
    if sort == compare:
        return True

# There is nothing smart going on here.
# This creates a list of all pandigital concatenations.


def concat(number):
    concat = ""
    for i in range(1, 50):
        hold = number * i
        concat += str(hold)
        if len(concat) == 9:
            if panDigitial(concat):
                return concat
        if len(concat) > 9:
            return False

# Initiates the loop
# Essentially, the roof is 10000, because 2x10000 concatenated with 10000
# is larger than 9-digits, and that will be true for all numbers above
# that so they are not candidates.


start = time.time()
myList = []
for i in range(1, 10000):
    if concat(i):
        myList.append(concat(i))

# Sorting the list will place the highest value at the end of the list,
# last line just prints the last item of that sorted list.

myList = sorted(myList)
elapsed = time.time() - start
print("Found %s in %s seconds" % (myList[-1], elapsed))
