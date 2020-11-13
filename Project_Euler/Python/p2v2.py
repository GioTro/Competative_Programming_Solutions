

#Problem_2 new version

import time

target = int(input("Sum all fibbonacci numbers lower than: "))

start = time.time()

fib = [1, 1]

while fib[-1]<target:
    fib.append(int(fib[-1]+fib[-2]))

fib = list(filter(lambda x: x<target, fib))


elapsed = (time.time() - start)

print("\n\nThe sum of all fibbonacci number below %s is %s.\n \n" % (str(target), sum(fib)))

print("Results found in %s seconds." % (elapsed))
