# tupla=[1,2,3,4,5]
# def to_list(tupla):
#     if type(tupla) == type((1,2,3)):
#         lista=[]
#         for x in range(0,len(tupla)):
#             lista.append(tupla[x])

#         return lista
#     else:
#         print("no se puede realizar la operacion ya que no es una tupla")
#         return None

# devo= to_list(tupla)
# print("la lista es", devo)

# Algoritmos de ordenamiento

lista_desordenada=[23, 1, 56, 15, 3, 0, 89, 156, 45]

def seleccion(lista_desordenada):
    for x in range(0,len(lista_desordenada)):
        minimo=x
        for z in range(minimo+1,len(lista_desordenada)):
            if lista_desordenada[z] < lista_desordenada[x]:
                minimo=z
                
        lista_desordenada[minimo], lista_desordenada[x] = lista_desordenada[x], lista_desordenada[minimo]

    return (lista_desordenada)


listafinal=seleccion(lista_desordenada)
print(listafinal)


# def insercion(lista_desordenada):
#     for i in range(len(lista_desordenada)):
#         for j in range(i,0,-1):
#             if(lista_desordenada[j-1] > lista_desordenada[j]):
#                 orden=lista_desordenada[j]
#                 lista_desordenada[j]=lista_desordenada[j-1]
#                 lista_desordenada[j-1]=orden

#     return (lista_desordenada)


# listafinal=insercion(lista_desordenada)
# print(listafinal)





# def intercambio(lista_desordenada): # burbuja
#     n = len(lista_desordenada) 
#     for z in range(n):
#         for j in range(0, n-z-1):
#             if lista_desordenada[j] > lista_desordenada[j+1] : 
#                 lista_desordenada[j], lista_desordenada[j+1] = lista_desordenada[j+1], lista_desordenada[j]
#     return (lista_desordenada)


# listafinal=intercambio(lista_desordenada)
# print(listafinal)
