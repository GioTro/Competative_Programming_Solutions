import time

### Solution works, but it has a runtime,
#problem, the problem is a bit out of my,
#knowledge it has a runtime of 12 hours,
#essentially bruteforcing it.

start = time.time()

def suma(n):
    return sum(int(x) for x in n)

def check(n):
    c = str(n)
    check = []
    compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0,9):
        check.append(int(c[i]))
    sort = sorted(check)
    if sort == compare:
        return True



a, b = 1, 1
d = 0

#Fib generator...

fib_index = 2
potential = []

while fib_index<278330:
    c = a + b
    a = b
    b = c
    fib_index += 1
    d += 1

while d>0:
    c = a + b
    a = b
    b = c
    fib_index += 1
    string = str(c)
    if check(string[0:9])==True:
        elapsed = time.time() - start
        print("first digits %s in fib.index %s %s" % (string[0:9], fib_index, elapsed))
    if check(string[-9:])==True:
        elapsed = time.time() - start
        print("last digits %s in fib.index %s %s" % (string[-9:], fib_index, elapsed))
    if check(string[0:9])==True and check(string[-9:])==True:
        print("fib-number %s first %s and last %s are 1-9 pandigital" % (fib_index, string[0:9], string[-9:]))
        break

elapsed = (time.time() - start)

print(elapsed)

input()
