# Series termination ....
# I want to avoid to check numbers twice but getting stuck, and realized,
# current approach will not work


import time
target = 10000

turbo = list(int(i) for i in range(1, target + 1))


start = time.time()


def square(n, retur=0):
    string = str(n)
    for i in range(0, len(string)):
        retur += int(string[i]) * int(string[i])
    return int(retur)


number = []

c = 145
i = len(turbo)

while True:
    c = turbo[i]
    while c != 1 or c != 89:
        c = square(c)
        i -= 1
        if c in turbo:
            turbo.remove(c)
            i -= 1
        if c == 1 or c == 89:
            number.append(c)
            break

count = len(list(number[i] for i in range(0, len(number)) if number[i] == 89))

elapsed = (time.time() - start)
print(
    "\nThe number of series that terminate at 89 is %s. Results found in %s seconds." %
     (count, elapsed))
