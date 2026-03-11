

######################################
## Welcome to Bloque_2: 
######################################

#--*Emplearemos 3 pasos esenciales 1.- Entrada de datos, 2.- Proceso de datos, 3.- Salida de datos*--
print("---Ejercicio python del bloque_2---")

##--Ejercicios Desarrollados Bloque 2: 

            
def numeros():
    print("100 primeros numeros naturales")
    for i in range(100):
        print(i)

def numeros_primos():
        print("Ingrese un número entero para imprimir si es primo o no:")
        num = int(input("Numero: "))
        primo = 0
        for i in range(1, num + 1):
            if num % 2 == 0:
                primo += 1
        if primo == 2:
                print("El numero ingresado si primo ")
        else:
            print("El numero ingresado no es primo: ")

def suma_numeros():
    print("Ingresa 10 números para sumarlos: ")
    try:
        suma = 0
        for i in range(1, 11):
            number = int(input(f"Número {i}: "))
            suma += number
        print(f"La suma de los 10 números es: {suma}")
    except ValueError:
        print("Error: Debes Ingresar un numero valido")

def suma_promedio():
    try:
    #Primero inicializamos variables 
        suma = 0
        i = 1
        n = int(input("Cuantos numeros quieres ingresar?: "))
        while i <= n:
            number = int(input(f"Ingresa el valor a {i}: "))
            suma += number
            i += 1
        promedio = suma/n
        print(f"La suma es {suma}: ")
        print(f"El promedio es: {promedio}: ")

    except ValueError:
        print("Ingrese un valor valido (solos numeros)")

def par_impar():
    print("Contador de par y impar de 5 numeros: ")
    try:
        pares = 0
        impares = 0
        i = 0
        while i < 6:
            num = int(input(f"Ingrese Numero {i + 1}: "))
            if num > 0:
                if num % 2 == 0:
                    pares += 1
                else:
                    impares += 1
                i += 1
            else:
             print("Ingrese valores positivos")
           
        print(f"Cantidad de numeros pares: {pares}")
        print(f"Cantidad de numeros impares: {impares}")
    except ValueError:
        print("Ingresa un valor valido")

def fibonacci():
    print(" La suma de los 10 primeros numeros de la serie Fibonacci: ")
    a = 0
    b = 1
    #Inicializamos la variable suma
    suma = 0
    for i in range(1, 11):
        suma += a
        print(f"Numero {i}: {a}")
        c = a + b
        a = b
        b = c
    print(f"La suma de {i} en la serie fibonacci es: {suma} ")

def comparacion_numeros():
    print("Cantidad de números pares, impares, positivos, negativos, neutros")
    print("Ingresa 5 números:")
    positivos = 0
    negativos = 0
    neutros = 0
    pares = 0
    impares = 0
    for i in range(5):
        number = int(input(f"Número {i+1}: "))

        if number > 0:
            positivos += 1
        elif number < 0:
            negativos += 1
        else:
            neutros += 1

        if number % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(
        f"Hay {positivos} positivos, {negativos} negativos, "
        f"{pares} pares, {impares} impares y {neutros} neutros"
    )

def suma_pares_impares():
    print("Ingrese la cantidad que deseas sumar: ")
    suma_par = 0
    suma_impar = 0
    num = int(input("Number: "))
    for i in range(num):
        dato = int(input(f"Number {i+1}: "))
        if dato % 2 == 0:
            suma_par += dato
        else:
            suma_impar += dato
    print(f"La suma de los pares es: {suma_par} y la suma de los impares es: {suma_impar}")

def menu():
    print("-----MENU-----")
    print("1.- Algoritmo que imprime 100 primeros valores")
    print("2.- Numeros primos")
    print("3.- Suma de 10 numeros")
    print("4.- Suma y promedio")
    print("5.- Fibonacci")
    print("6.- par y impar")
    print("7.- Comparacion de numeros; P, N, P, I y N")
    print("8.- Suma de pares y impares: ")
    print("9.- Salir: ")

while True:
    menu()
    try: 
        #Opcion que ingresaran los usuarios 
        option = int(input("Ingresa una opcion: "))
    except:
        print("La opcion es incorrecta Ingrese un nuevo valor: ")
        continue
    match option:
         case 1:
              numeros()
         case 2:
              numeros_primos()
         case 3: 
              suma_numeros()
         case 4:
              suma_promedio()
         case 5:
            fibonacci()
         case 6:
            par_impar()
         case 7:
            comparacion_numeros()
         case 8: 
            suma_pares_impares()
         case 9: 
            print("Saliendo del programa")
            break

    