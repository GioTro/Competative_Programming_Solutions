
import time

start = time.time()

def function(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

f=0
numbers = []

for i in range(1,1000000):
    binary = str(bin(i)[2:])
    number = str(int(i))
    if function(binary)==True and function(number)==True:
        f+=1
        numbers.append(i)

elapsed = (time.time() - start)


print("There are %s numbers that are palindromic in both base10 and base2 less than one million, these are %s. Result found in %s seconds." %
      (f, numbers, elapsed))

            
        


