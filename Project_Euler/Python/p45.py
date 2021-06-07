import time
import logging

logging.basicConfig(level=logging.DEBUG)
start = time.time()

Triangle = []
Hexagonal = []
Pentagonal = []


def tri(number):
    varA = int(number) + 1
    Tn = int(number) * varA / 2
    return int(Tn)


def pent(number):
    varA = 3 * int(number) - 1
    Pn = int(number) * varA / 2
    return int(Pn)


def hexa(number):
    varA = 2 * int(number) - 1
    Hn = int(number) * varA
    return int(Hn)


i = 1

# This was slow =>

# while True:
#    Triangle.append(tri(i))
#    Hexagonal.append(hexa(i))
#    Pentagonal.append(pent(i))
#    matches = list(x for x in Triangle if x in Hexagonal and x in Pentagonal)
#    i += 1
#    if len(matches)==3:
#        break

matches = []

# Marginally faster =>

while True:
    Pentagonal.append(pent(i))
    Hexagonal.append(hexa(i))
    i += 1
    if Pentagonal[-1] > 10**10 and Hexagonal[-1] > 10**10:
        logging.debug("Done!")
        break

i = 1
index = []
while True:
    turn = tri(i)
    if turn in Pentagonal and turn in Hexagonal:
        matches.append(turn)
        index.append(i)
    if len(matches) == 3:
        break
    if turn > Hexagonal[-1] and turn > Pentagonal[-1]:
        logging.debug("Dead!")
        break
    i += 1


#index = []
# for i in range(0, len(matches)):
#    index.append(int(Triangle.index(matches[i]))+1)


elapsed = (time.time() - start)

#print("The number %s is the %sth Triangle number that is also a Pentagonal and Hexagonal number! Results found in %s seconds!" % (Triangle[index[1]-1], index[1], elapsed))

print("The number %s is the %sth Triangle number that is also a Pentagonal and Hexagonal number! Results found in %s seconds!" %
      (matches[-1], index[-1], elapsed))

# Works, returns answer in 108 seconds.
