#Problem 6 s'o'nder bantad

#Hm, it this implimitation is 6 microseconds faster than
#The original version if "time" can be trusted

import time

start = time.time()

SumSquare = sum(list(i**2 for i in range(1, 100+1)))

SumInt = sum(list(i for i in range(1,100+1)))**2

result = SumInt - SumSquare

elapsed = (time.time() - start)

print("Result: %s ---- found in %s" % (result, elapsed))
