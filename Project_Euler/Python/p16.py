

number = str(2**1000)
suma = []

for i in range(0, int(len(str(number)))):
    suma.append(int(str(number)[i]))

print(sum(suma))
