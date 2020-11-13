import time

start = time.time()

factorial = 1

for i in range(1, 100):
    factorial *= i

print(factorial)
digitString = str(factorial)
suma= []

for i in range(0, len(str(digitString))):
    suma.append(int(str(digitString)[i]))

elapsed = (time.time() - start)

print("The sum %s in %s seconds" % (sum(suma),elapsed))
    
