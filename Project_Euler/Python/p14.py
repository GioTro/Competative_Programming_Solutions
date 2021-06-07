

def function(n, count=1):
    while n > 1:
        count += 1

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count


max = [0, 0]

for i in range(1000000):
    c = function(i)
    if c > max[0]:
        max[0] = c
        max[1] = i

print(max)
