# Problem 56
# Old implementantion is commented out
import time

start = time.time()


def checksum(n):
    #suma = []
    Summm = list(int(str(n)[i]) for i in range(0, int(len(str(n)))))
    # for i in range(0, int(len(str(n)))):
    # suma.append(int(str(n)[i]))
    return sum(Summm)


max = 0

for i in range(1, 100 + 1):
    for j in range(1, 100 + 1):
        #number = i**j
        number = int(checksum(i**j))
        if number > max:
            max = number

elapsed = (time.time() - start)
print(
    "\nSum of digits la la la is %s. Results found in %s seconds.\n\n" %
     (max, elapsed))
