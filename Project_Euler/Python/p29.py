lista = []

for i in range(2, 101):
    for j in range(2, 101):
        lista.append(int(i**j))


print(len(list(set(lista))))
