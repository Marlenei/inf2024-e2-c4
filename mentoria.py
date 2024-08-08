# Crea una lista a partir de otra lista.

# Funciones de listas:
#         Usa la función len() para obtener la longitud de una lista.
#         Usa la función in para verificar si un elemento está en una lista.
#         Usa la función index() para encontrar la posición de un elemento en una lista.
#         Usa la función append() para agregar un elemento al final de una lista.
#         Usa la función insert() para insertar un elemento en una posición específica de una lista.
#         Usa la función remove() para eliminar un elemento de una lista por su valor.
#         Usa la función pop() para eliminar un elemento de una lista por su índice y obtenerlo de vuelta.
#         Usa la función sort() para ordenar los elementos de una lista.
#         Usa la función reverse() para invertir el orden de los elementos de una lista.
#         Usa la función copy() para copiar una lista.

# Listas anidadas:
#         Crea una lista de listas.
#         Accede a elementos de listas anidadas.
#         Modifica elementos de listas anidadas.

# Ejercicios de aplicación:
#         Crea un programa para almacenar y administrar una lista de compras.


#--------------------------------------------------------------------------

# lista=[12,3,6,56,5,8498,5265,878]
# print(lista)
#         Obtén el primer elemento de una lista.
# print(lista[0])

#         Obtén el último elemento de una lista.
# print(lista[-1])

#         Obtén un elemento específico de una lista por su índice.
## print(lista[2])

#         Obtén un subconjunto de una lista (slicing).
# print(lista[0:3])

# Modificación de listas:
#         Agrega un elemento al final de una lista.
# agregado=input("ingrese el elemento ")
# lista.append(agregado)

#         Inserta un elemento en una posición específica de una lista.
# agregado2=input("ingrese el elemento ")
# indice2=int(input("ingrese el indice del elemento que desea "))
# lista.insert(indice2,agregado2)


#         Elimina un elemento de una lista por su índice.
# indice3=input("ingrese el indice del elemento que desea eliminar ")
# ind=int(indice3)
# lista.pop(ind)
# print(lista)

#         Remplaza un elemento de una lista por otro.
# valor1=int(input("ingrese el  elemento que desea cambiar "))
# indice4=int(input("ingrese el indice del elemento que desea eliminar "))
# lista[indice4]=valor1
# print(lista)

#--------------------------------------------------------------------------------------

# Operaciones con listas:
lista=[1,2,3,4,5]
lista2=[6,7,8,9,10]
#         Une dos listas.
lista3=lista + lista2
print(lista3)
#         Verifica si un elemento está en una lista.
# valor2=int(input("ingrese el elemento que desea verificar "))
# for x in range(0,len(lista3)):
#     if valor2 == lista3[x]:
#         print("si se encuentra")
#     else:
#         print("no se encuentra")

#         Obtén la longitud de una lista.
# print(len(lista3))

#         Invierte el orden de los elementos de una lista.
# print(list(reversed(lista3)))

#         Ordena los elementos de una lista.
