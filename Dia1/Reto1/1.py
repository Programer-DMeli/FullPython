#- Programa que pida al usuario un numero n como cantidad de numeros aleatorios que se almacenaran en una lista, esta lista debe imprimirse y crear otra lista donde se alamacenaran los numeros que no
#se repiden en la lista genreral, teniendo que eliminar los numeros que se repiten.

import random

try:

    print("Programa que imprime el numero de veces que se repite un numero en una lista")
    limite = int(input("Ingresa e numero limite: "))
    lista_general = [random.randint(0, 100) for i in range(limite)]

    lista_nueva = []
    for num in lista_general:
        if num not in lista_nueva:
            lista_nueva.append(num)
    print("\n" + "="*30)
    for numero in lista_nueva:
        veces = lista_general.count(numero)
        if veces > 1:
            print(f"El numero {numero:2} se repite {veces} veces y se elimina {veces - 1} elemento ") #numero:2 nos permite alinear los numeros a la derecha
    print("\n" + "="*30)
    print("Lista general")
    for i in lista_general:
        print(i, end=" ")


    print("Lista nueva ")
    for i in lista_nueva:
        print(i, end=" ")
    #contamos cuantos veces aparece en la lista general

except ValueError:
    print("Ingrese un numero valido")


