from functools import reduce

tupla = [1, 2, 3, 4, 5]

suma = sum(tupla)
longitud = len(tupla)
maximo = max(tupla)
minimo = min(tupla)
ordenar = sorted(tupla)
reversa = list(reversed(tupla)) # tupla[::-1]
enumerar = list(enumerate(tupla))
mapear = list(map(lambda x: x + 3, tupla))
mapRed = reduce(lambda x, y: x + y, tupla)
filtrado = list(filter(lambda x: x % 2 == 0, tupla))


print("Suma: ", suma)
print("Longitud: ", longitud)
print("Maximo: ", maximo)
print("Minimo: ", minimo)
print("Ordenado: ", ordenar)
print("Reversa: ", reversa)
print("Enumerar: ", enumerar)
print("mapear: ", mapear)
print("mapRed: ", mapRed)
print("Filtrado: ", filtrado)


# insert() remove() append() pop() count()
# tupla = (1,2,3,4,5,4,4,4,4)
# lista = list(tupla)
# lista.insert(0,38)
# tupla = tuple(lista)
# print(tupla)

# lista.remove(3)
# print(lista)

# lista.append(333)
# print(lista)

# lista.pop()
# print(lista)

# ocurrencias = lista.count(4)
# print(ocurrencias)