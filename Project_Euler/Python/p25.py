#Index of the first fibnmr>1000digits


def fiblist(n):
    fib = [1,1]
    i = 2
    c = 0
    b=0
    
    while i<=n:
        fib.append(fib[i-1]+fib[i-2])
        i += 1
    else:
        fib2 = list(filter(lambda x: x>10**999, fib))


    while c<1:
        b+=1
        if fib[b]==fib2[0]:
            print(b+1)
            print(fib[b])
    else:
        c+=1
    return
        





fiblist(5000)


