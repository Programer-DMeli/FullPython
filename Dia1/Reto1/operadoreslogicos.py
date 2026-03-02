
#---Quiz 1: Operadores lógicos---
print("-- MENU DE FIGURAS GEOMETRICAS CON BUCLES ANIDADOS --")

def cuadrado(rows, cols): #Funcion que pide como parametro 2 números para la columna y par la fila
    for _ in range(rows):
        for _ in range(cols):
            print("*", end=" ")
        print()

def rectangulo(rows, cols):
    for _ in range(rows):
        for _ in range(cols):
            print("*", end=" ")
        print()

def triangulo(n):
    for i in range(1, n + 1):
        print("*" * i)

def triangulo_invertido(n):
    for i in range(n, 0, -1):
        print("*" * i)

def cuadrado_vacio(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

def triangulo_rectangulo(n):
    for i in range(1, n + 1): 
        print("*" * i)

while True:
    print("--Menu---")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Triangulo invertido")
    print("5. Cuadrado hueco")
    print("6. Triangulo Rectangulo")
    print("7. Salir")

    try:
        option = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Opción inválida. Ingresa un número.")
        continue

    match option:
        case 1:
            print("Cuadrado")
            cuadrado(5, 4)
        case 2:
            print("Rectangulo")
            rectangulo(4, 6)
        case 3:
            print("Triangulo")
            triangulo(5)
        case 4:
            print("Triangulo invertido")
            triangulo_invertido(5)
        case 5:
            print("Cuadrado hueco")
            cuadrado_vacio(5)
        case 6:
            print("Triangulo Rectangulo")
            triangulo_rectangulo(5)
        case 7:
            print("Saliendo del programa")
            break
        case _:
            print("Opción no reconocida. Intenta de nuevo.")

            
