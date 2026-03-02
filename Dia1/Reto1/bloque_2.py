#--Primer ejercicio de nuestra semana de full Python--
print("Mi primer ejercicio con operadores lógicos")
### Ejercicio 1: Ingrese un número entero y luego visualice un mensaje indicando si es “primo” o
#  “no primo”. Emplee while y for para resolver el ejercicio.--

######################################
######################################

#--*Emplearemos 3 pasos esenciales 1.- Entrada de datos, 2.- Proceso de datos, 3.- Salida de datos*--

#--1.- Entrada de datos--#
    #Pedimos al usuario que ingrese un número entero y lo almacenamos en la variable num.

#--2.- Proceso de datos--#
    #Utilizamos un for para recorrer el rango de números desde 1 hasta el número ingresado, y un contador para contar cuántos divisores tiene el número.

#--3.- Salida de datos--#
     #Son primos o no son primos dependiendo del numero de divisores.
print("Ingrese un número entero:")
num = int(input("iNGRESE UN NUMERO: "))
if num > 1:
   count = 0
   for i in range(1, num + 1):
        number = num % i
        if number == 0:
            count += 1 
else:
    print("Ingrese un numero mayor a 1")

if count == 2:
    print("El número es primo")
else: 
    print("El número no es primo")
