#1

# edad = int(input("Ingrese su edad "))

# if edad >= 18: 
#     print("es mayor")

# else:
#     print("es menor")


#2
# numero = int(input("Ingrese un numero "))

# rest=numero%5

# if rest==0:
#     print("es multiplo")

# else:

#     print ("no es multiplo")

#3

# numero1 = int(input("Ingrese un numero "))
# numero2 = int(input("Ingrese un numero "))

# if numero1 > numero2:
#     print("es mayor ", numero1)

# else:

#     print ("es mayor ", numero2)


#4
# numero = int(input("Ingrese el año "))

# rest=numero%4

# if rest==0:
#     print("es bisiesto")

# else:

#     print ("no es bisiesto")

#5
# numero = int(input("Ingreso el monton de la compra "))


# if numero >= 100:
#     descuento = numero -(numero * 0.10)
#     print("Monto a pagar ", descuento)

# else:

#     descuento = numero -(numero * 0.05)
#     print("Monto a pagar ", descuento)


#6 Calificar una nota. Se ingresará notas en valores de 0 a 100. Mostrar si la calificación es A (mayor o igual a 90), 
# B (mayor o igual a 80), C (mayor o igual a 70), D (mayor o igual a 60) o F.



# numero = int(input("Ingrese la nota "))
# if numero >= 90 and numero <= 100:
#     print("Su nota es A")

# elif numero >= 80 and numero <= 89:
#     print("Su nota es B")
# elif numero >= 70 and numero <= 79:
#     print("Su nota es C")
# elif numero >= 60 and numero <= 69:
#     print("Su nota es D")
# elif numero <=59:
#     print("Su nota es F")
# else:
#     print("Numero incorrecto")

#7
# letra = str(input("Ingrese la letra "))
# letra1 = letra.lower()

# if letra1 =="a" or letra1=="e" or letra1=="i" or letra1=="o" or letra1=="u":
#     print("Es vocal ")

# else:
#     print("es consonante")

#8
# rango1 = int(input("Ingrese el minimo de rango "))
# rango2 = int(input("Ingrese el maximo de rango "))
# numero = int(input("Ingrese el numero "))

# if numero >= rango1 and numero <= rango2:
#     print("Esta dentro del rango")
# else:
#     print("Esta fuera del rango")


#9
# for x in range (100,116):
#     print(x)

#10
# for x in range (0,21):
#     res=x%2
#     if res==0:
#      print(x)

#11
# acumulador=0
# for x in range (0,101):
#     acumulador += x

# print (acumulador)

#12
# numero = int(input("Ingrese el numero "))

# acumulador=1
# for x in range (1,numero+1):
#     acumulador *= x

# print(acumulador)

#13
# iniFibo = 0
# finFibo = 1
# for x in range(0,10):
#     finFibo = finFibo + iniFibo
#     iniFibo = finFibo - iniFibo
#     print(iniFibo)

#14
# numero = int(input("Ingrese el numero "))
# print (len(str(numero)))

#15
# acumulador=0
# for x in range(0,5):
#     numero = int(input("Ingrese el numero "))
#     acumulador+=numero

# promedio=acumulador/5
# print("el promedio es ",promedio)

#16
# maximo=-999999
# for x in range(0,11):
#     numero = int(input("Ingrese el numero "))
#     if numero>maximo:
#         maximo=numero

# print("el numero mas alto es", acumulador)

#17
# inicio = int(input("Ingrese el inicio del rango "))
# fin = int(input("Ingrese el fin del rango "))
# for x in reversed(range(inicio,fin)):
#     print(x)

