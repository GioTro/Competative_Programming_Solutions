

def function(n):
    a = 0
    odd = []
    numbers = []
    while a < n:
        a += 1
        numbers.append(a)
        if a % 2 == 1:
            odd.append(a)
    if a == n:

        i = 0
        while i < n:
            if check(odd[i]) == False:
                i += 1
            else:
                print(odd[i])


def check(n):
    if (lambda x: 7 + 2 * x**2 == n and n > 2, range(1, 9)):
        return True
    else:
        return False


function(10)
