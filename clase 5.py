from functools import reduce

lista = [1, 2, 3, 4, 5]

suma = sum(lista)
longitud = len(lista)
maximo = max(lista)
minimo = min(lista)
ordenar = sorted(lista)
reversa = list(reversed(lista)) # lista[::-1]
enumerar = list(enumerate(lista))
mapear = list(map(lambda x: x + 3, lista))
mapRed = reduce(lambda x, y: x + y, lista)
filtrado = list(filter(lambda x: x % 2 == 0, lista))


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



# any() all() SOLO PARA BOOLEANOS
lista = [True, True, True, True]

# any_list = any(lista) que al menos 1 elemento este en TRUE
# print("Any:", any_list)

# all_list = all(lista) que TODOS esten en TRUE
# print("All:", all_list)

# zip()
# lista_1 = [1,2,3]
# lista_2 = ['a','b','c']

# lista_cpx = list(zip(lista_1, lista_2))
# print(lista_cpx)

# insert() remove() append() pop() count()
lista = [1,2,3,4,5,4,4,4,4]
lista.insert(0, 38)
print(lista)

lista.remove(3)
print(lista)

lista.append(333)
print(lista)

lista.pop()
print(lista)

ocurrencias = lista.count(4)
print(ocurrencias)

print(f"""
      s
      sd
      sd
      sd
      fs
      df
      sdf
      fgd""")