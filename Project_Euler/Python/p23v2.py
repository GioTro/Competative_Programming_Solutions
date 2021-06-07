import time

start = time.time()


def abundant(n):
    sum = 0
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            sum += 1
    if sum > n:
        return True
    else:
        return False


def abundant_sum(n):
    for i in abundants:
        if i > n:
            return False
        if (n - i) in abundants:
            return True
        else:
            return False


abundants = [x for x in range(1, 28123 + 1) if abundant(x)]

result = (sum(x for x in range(1, 28123 + 1) if not abundant_sum(x)))

elapsed = (time.time() - start)

print("result %s returned in %s seconds." % (result, elapsed))
