# lista = [1,2,3,4,5]

# sumatotal=0

# for suma in lista:
#     sumatotal += suma        --------- forma 1


# print(sumatotal)




# suma = sum(lista) -------- forma 2
# print (suma)



# cadena = input("Ingrese una cadena de texto: ")

# if cadena == cadena [::-1]:
#      print('Es un palíndromo')
# else:
#     print('No es un palíndromo')



lista = [1,3,6,1,87,123,1,32]

# max_lista = max(lista)
# print("numero mas alto es:", max_lista)
    
aux = lista[0]
for i in lista:
    if i > aux:
        aux = i

print(aux)