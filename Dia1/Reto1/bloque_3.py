import random
###--Ejercicio del bloque 3 ##
#####################################
##---Full Ejercicios con Listas--####
#####################################

#-- 3 procesos escenciales
#--Entrada
#--Proceso
#--Salida 

#-- Para actualizar valores utilizamos 
# name.append(valor) -> Sirve para agregar valores al final
# name.extend(name2) -> Sirve para anidar valores entre dos listas
# name.insert(indice, valor) -> Sirve para añadir valores en posiciones expecificas y cuando es con - se añade delante del valor
# name.remove(valor). -> Elimina la primera aparicion de un valor en una lista
# elemento = name.pop() -> Elimina el ultimo elemento si no le entregas un indice, tambien devuelve su valor eliminado sin o con indice
# del name  -> es un declaracion que sirve par eliminar partes de una lista
###--OPERACIONES BASICAS EN LISTA--##
#- variable = name.count(valor a contar)-> Devuelve el numero de veces que un valor se encuentra en una lista. 
#- longitud = len(lista) -> Devuelve el numero de longitud de una lista. 
#- lista.short() -> Ordena los elementos de la lista, con reverse = True
#- Clear -> elimina todos los elementos de la lista 
#- Sum(lista) -> Devuelve a la suma de todos los elementos 
#- max(lista) -> imprime el maximo
#- min(lista) -> imprime el minimo
#  + Se utiliza como operador de concatenacion entre 2 listas a mas  
# - name.index("valor") -> Duelve el indice en el que se encuentra el valor
#- name.reverse() -> Invierte el orden de la lista



print("Ejercicios de Listas")

def menu():
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Salir")

def ejercicio_1():
    print("Ejercicio 1")
    lista = [1, 2, 3, 4, 5]
    print(lista)
    lista.append(6)
    print(lista)
    lista.extend([7, 8, 9])
    print(lista)
    lista.insert(0, 0)
    print(lista)
    lista.remove(0)
    print(lista)
    elemento = lista.pop()
    print(elemento)
    print(lista)
    del lista[0]
    print(lista)
    lista.clear()
    print(lista)

def ejercicio_2():
    #--Registramos datos de Entrada
    print("Recorriendo datos con for y While")
    colores = ["rojo", "azul", "verde", "amarillo", "morado"]
    for color in colores:
        print(color) #forma vertical, para forma horizontal se usa end=""
    print() #-Sirve pada dar espacio entre los ejercicios
    contador = 0
    while contador < len(colores):
        print(colores[contador], end=" ")
        contador += 1

def ejercicio_3():
    print("Ejercicio 3")
    #Crear un progrma que ingresa 5 numeros y calcular la suma y el promedio
    numeros = [] #inicializamos la lista vacia
    print("Ingresar 5 numeros: ")
    for i in range(5):
        valor = float(input(f"Ingresa el numero {i+1}: "))
        numeros.append(valor) #- Ingresamos los valores a la lista 
    #Hallamos la suma
    suma = sum(numeros)
    #Hallamos el promedio
    promedio = suma / len(numeros)
    print(f"La suma de los numeros es: {suma}")
    print(f"El promedio de los numeros es: {promedio}")

def ejercicio_4():
    print("Ejercicio 4")
    # Creamos un progrma que ingrese 5 numeros al final imprimir el minimo y el maximo
    print("Ingresar 5 numeros: ")
    number = [] #Lista vacia
    for j in range(5):
        variable = float(input(f"Ingresa el numero {j+1}: "))
        number.append(variable)
    #utilizamos las funciones max y min
    print(f"El numero mayor es: {max(number)}")
    print(f"El numero menor es: {min(number)}")

def ejercicio_5():
    print("Ejercicio 5")
    #Crear un programa que ingrese 5 numeros y los ordene de forma ascendente con fot y descendente con while
    dato = [] #Inicializamos la lista vacia
    print("Ingresar 5 nombres: ")
    #Ingreso de nombres
    for i  in range(5):
        variable = input(f"Ingrese el valor {i+1}: ")
        dato.append(variable)
    print()
    #Imprimir de manera  ascendente
    
    dato.sort()
    print("Datos ordenados de forma ascendente: ")
    for i in dato:
        print(i, end=" ")
    print()

def ejercicio_6():
    print("Utilizaremos un arreglo para almacenar los numeros pares e impares Ingresados por el usario")
    # Pediremos al usuario que ingrese el valor de n, el cual respresentara el valor final de interacion
    try:
        num = int(input("Ingresa el valor de n: "))
        numeros = []
        #- Almacenamos los datos en la lista
        for i in range(num):
           #comprobamos que sea positivo
           while True: #nos garantiza que se ingrese un numero positivo y no se gaurde el numero ingresado en la lista
               numero = int(input(f"Ingresa el numero {i+1}: "))
               if numero > 0:
                   numeros.append(numero) #-Con esto solo se ingresaran datos a la lista que sean positivos
                   break #Permite salir del while cuando el dato sea valido
               else:
                   print("Ingresa un numero positivo o mayor a cero")

        #-Para un codigo mas limpio utilizamos list comprehesion y utilizamos una condicion para separar los numeros pares e impares de la lista general
        par = [n  for n in numeros if n % 2 == 0] #- n es el valor que guardaremos en la nueva lista cada vez que n en numeros cumple la condicion
        impar = [n for n in numeros if n % 2 != 0]
       #-Salida de datos 
        print(f"cantidad pares {len(par)}, Cantidad impares {len(impar)}")
        for i in range(len(par)):
            print(f"Numeros pares: {par[i]}")
        print()
        for i in range(len(impar)):
            print(f"Numeros impares: {impar[i]}")

    except ValueError:
        print("Ingresa un valor valido")
    finally:
        print("Ejecutando limpieza")
    
def ejercicio_7():
    n_limite = int(input("Ingresa el valor de n; "))
    pares = []
    if n_limite > 0:
        print("Numeros pares entre ")
        for i in range(0, n_limite + 1):
            if i % 2 == 0:
                pares.append(i)
        print(f"Numeros pares del arreglo {pares} ")
    else:
        print("Ingrese un valor positivo ")

def ejercicio_8():
    print("Imprimimos numeros aleatorios")
    numeros_aleatorios = []
    numeros_divididos  = []
    number = int(input("¿Cuantos numeros aleatorios quieres imprimir? "))
    for i in range(number):
        variable = random.randint(1, 100)
        numeros_aleatorios.append(variable)
        numeros_divididos.append(variable / 2)
    #- Utilizamos un for para imprimir los datos de la lista
    for i in range(number):
        print(f"Numero aleatorio {i+1}: {numeros_aleatorios[i]}, {numeros_divididos[i]}")

def ejercicio_9():
    print("Programa que separa numeros positivos y negativos a partir de una lista")
    try:
        number = int(input("¡Cuantos numeros quieres ingresar! ")) 
        dato_numerico = []
        for i in range(number):
        
         while True:
            try:
                dato = int(input(f"Ingresa un numero {i+1}: "))
                dato_numerico.append(dato)
                break #Salimos del bucle para volver al iterador del for
            except ValueError:
                 print("Error: Ingresa un dato nuemrico")
        positivos = [num for num in dato_numerico if num >= 0]
        negativo = [ num for num in dato_numerico if num < 0]

    #Imprimimos los valores
        print("Numeros positivos")
        for n in positivos:
            print(n, end=" ")
        print()
        print("Numeros negativos")
        for n in negativo: 
            print(n , end=" ")
    except ValueError:
        print("Ingresa un valor numerico")
    finally:
        print("Ejecutando limpieza")


def ejercicio_10():
    print("Programa que imprime los estudiantes con notas_altas y notas_bajas")
    try: 
        n_limite = int(input("¿Cuantos estudiantes desea ingresar: "))

        nombres_estudiante = []
        notas_estudiante = []

        for i in range(n_limite):
            nombre = input(f"Ingresa el nombre del estudiante {i+1}: ")
            notas = float(input(f"Ingresa la nota del estudiante {i+1}: "))
            nombres_estudiante.append(nombre)
            notas_estudiante.append(notas)

#Recorremos con un for cada indice y actualizamos las notas_bajas y notas_altas, para encontrar una relacion con los indeces de la lista nombre_estudiantes

        nota_alta = notas_estudiante[0] #El cero representa al primer estudiante ingresado el cual nos sevira como comparacion con otras notas ingresadas mas adelante
        nota_baja = notas_estudiante[0] 

        for nota in notas_estudiante:
            if nota > nota_alta: #Encontre un dato mayor a mi dato inicial y proceso a actualizar la variable 
                nota_alta = nota #Con esto actualizamos las varaibles
            if nota < nota_baja: #Encontre un dato menor a mi dato inicial y proceso a actualizar la variable
                nota_baja = nota
    
# utlizamos un bucle for para recorrer los indices de las listas y encontrar la relacion //Indentificacion de datos
        print("Estudiantes con notas altas: ")
        for i in range(n_limite):
            if notas_estudiante[i] == nota_alta: #Si econtramos una nota alta, imprimimos el nombre del estudiante
                print(f"{nombres_estudiante[i]}")


        print("Estudiantes con notas bajas: ")
        for i in range(n_limite):
            if notas_estudiante[i] == nota_baja:
                print(f"{nombres_estudiante[i]}")
    except ValueError:
        print("Ingresa un dato valido ")

def ejercicio_11():

    print("Programa que imprime y compara datos aleatorios")
    try:
        limite = int(input("Ingresa el nuero limite: "))
    
        numeros_aleatorios_1 = [random.randint(0,100) for i in range(limite)]
        numeros_aleatorios_2 = [random.randint(0,100) for i in range(limite)]

    #Imprimimos los numeroos aleatorios de la lista 1
        print("Numeros aleatroios de la lista 1")
        for i in numeros_aleatorios_1:
            print(i)

    #Imprimimos los numeros aleatorios lista_2
        print("Numeros aleatorios de la lista 2")
        for i in numeros_aleatorios_2:
            print(i)
        print("\n" + "="*30)
    #Utilizamos un bucle for para recorrer los datos de la lista 1 y comparar con la lista 2
        repetidos = []
        for numero in numeros_aleatorios_1:
            if numero in numeros_aleatorios_2:
                repetidos.append(numero) #Imprimimos el numero que se repite en las 2 listas"i)
    
        if len(repetidos) > 0:
            print("Numeros repetidos en las 2 listas: ")
            for num in repetidos: #num recorre indice por indice en repedidos para imprimir los datos
                print(num) # nos permite imprimir el valor del indice
        else:
            print("No hay numeros repetidos")
    except ValueError:
        print("Ingresa un dato valido")

def ejercicio_12():
    print("Porgrama que permite un juego al usuario de adivinar un numero entre 0 y 100")
    try: 
    #Desarollamos el juego:
        print("===Juego Retador: Adivina===")
        while True:
            n_limite = int(input("Ingresa la canidad de numero aleatorios que deseas generar: "))
            # generamos en nuestra lisTa los numeros aleatorios con list comprehesion 
            numeros_aleatorios = [random.randint(0, 100) for i in range(n_limite)]
            print("ingresa 1, 2, 3 , 4 rondas | 5.- para salir ")
            puntos = 0
            opcion = int(input("Ingresa una opcion: "))
            if opcion == 5:
                print("Saliendo del juego")
            break
            contador = 1
            while contador <= opcion:
                print(f"Ingrese la opcion {contador} de {opcion}: ")
                num_adivinador = int(input("¿Que numeros crees que este entre 0 y 100: "))
                if num_adivinador in numeros_aleatorios:
                    print(f" + 1 punto -> el numero que adivinaste es: {num_adivinador}")
                    puntos += 1
                else:
                    print(" -1 punto")
                    puntos -= 1
                contador += 1

            if puntos > 0: 
                print("Felicidades has ganado el juego")
                print(f"Tu puntaje es: {puntos}")
            else:
                print("Sigue intentando bro")
                print(f"Tu puntaje es: {puntos}")
            print("\n" + "="*30)
            print(f"Los numeros aleatorios son: {numeros_aleatorios}")
            print("\n" + "="*30)
    except ValueError:
        print("Ingresa un dato valido")
    print("Gracias por jugar, hasta pronto")

def ejercicio_13():
    print("Programa que ordena valores positivos y negativos")
    try: 
        n_limite = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
        numeros = []
        for i in range(n_limite):
            num = int(input(f"Ingrese el numero {i+1}: "))
            numeros.append(num)
    #clasificamos los numeros positivos y negativos con el metodo de list comprehesion
        negativos = []
        positivos = []
        for num in numeros:
            if num < 0:
                negativos.append(num)
            
            else:
                positivos.append(num)
        print("\n"+"="*30)   
        print(f"Hay {len(positivos)} numeros positivos")
        print(f"Hay {len(negativos)} numeros negativos")
    #Ordenamos los valores positivos y negativos de mayor a menor
        negativos.sort() #-Ordenamos los valores con sort
        positivos.sort()
        print("Numero negativos")
        for i in negativos:
            print(i, end=" ")
        print()
        print("Numeros positivos")
        for i in positivos:
            print(i, end=" ")

    #Imprimimos los valores positivos y negativos ordenados de nenor a mayor
    except ValueError:
        print("Error: Ingresa valores validos")

while True:
    print("Menu")
    menu()
    try:
        opcion = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Ingresa un valor valido")
        continue
    match opcion:

        case 1:
            ejercicio_1()
            
        case 2: 
            ejercicio_2()
        case 3:
            ejercicio_3()
        case 4:
            ejercicio_4()
        case 5:
            ejercicio_5()
        case 6:
            ejercicio_6()
        case 7:
            ejercicio_7()
        case 8:
            print("Saliendo del programa")
            break
        case _:
            print("Opcion no valida")



