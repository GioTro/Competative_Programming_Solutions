

def check(n):
    string = str(n)
    x = 2
    a = 0
    b = 1
    while True:
        if int(string[x])==0:
            x+=1
        else:
            if int(string[x:x+a])!=int(string[x+a:x+b]):
                a+=1
                b+=1
            if int(string[x:x+a])==int(string[x+a:x+b]) and int(string[x:x+a])!=int(string[x+a+1:x+b+1]):
                return int(a)
                break

max = 0

for i in range(2, 1000+1):
    x = 1/i
    c = check(x)
    if c>max:
       c = max

print(max)
