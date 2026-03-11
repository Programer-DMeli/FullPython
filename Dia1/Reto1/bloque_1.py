
import math
from getpass import getpass 



#--2.- Ejercicio: Crear una aplicación en Python que calcule el área de un circulo--

#--Datos de Entrada--#
    #--Pediremos al usuario que ingrese el radio del circulo

#--Proceso de Datos--#
    #--Utilizaremos la formula del area del circulo de A = pi*r2 

#--Salida de Datos--#
    #--Mostraremos el resultado del area del circulo--

################--MENU DE EJERCICIOS PARA COMPRENDER LOS FUNDAMENTOS DE PYTHON--################
print("---Menu de ejercicios  Python del bloque_1---")


def area_circulo():
    print("Ingrese el radio del circulo:")
    radio = float(input("Radio: "))
    area_circulo = math.pi * radio ** 2
    print(f"El area del circulo es {area_circulo:.2f}")

def area_cuadrado():
    print("Ingrese el lado del cuadrado:")
    lado = float(input("Lado: "))
    area_cuadrado = lado ** 2
    print(f"El área del cuadrado es: {area_cuadrado:.2f}")

def par_impar():
    print("Calculando par o Impar")
    number = int(input("Ingresa un numero: "))
    if number % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

def hipotenusa ():
    print("Ingrese el valor del cateto a: ")
    cateto_a = float(input("Cateto a: "))
    print("Ingrese el valor del cateto b:")
    cateto_b = float(input("Cateto b: "))
    hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
    print(f"La hipotenusa es: {hipotenusa:.2f}")


def interes():
    tiempo = 5
    print("Interes simple de inversion: ")
    sueldo = float(input("Ingrese su sueldo: "))
    tasa_interes = float(input("Ingrese la tasa de interes mensual: "))
    interes_simple = sueldo * (tasa_interes / 100)*tiempo
    Monto_final = sueldo + interes_simple
    print(f"El monto final de su inversion es: {Monto_final:.2f}")

def comparacion_numeros():
    print("Comparacion de 3 numeros")
    a = int(input("Ingresa el valor de A: "))
    b = int(input("Ingresa el valor de b: "))
    c = int(input("Ingresa el valor de c: "))
    if a > b and a > c:
        print(f"El mayor es: {a} ")
    elif b > a and b > c: 
        print(f"EL numero mayor es: {b}")
    elif c > a and c > b:
        print(f"El numero mayor es {c}")
    else: 
        print("Los numeros son iguales") 

def contraseña(): 
    print("--Vereficacion de contraseña--")
    password = getpass("Contraseña: ") #-Utilzamos getpass para ocultar el ingreso de la contraseña por la consola 
    if len(password) < 6:
        print("La contraseña es corta y insegura ")
    elif password == "codeprime":
        print("La contraseña es correcta: ")
    else:
        print("La contraseña es incorrecta: ")


def menu():
    print("1. Area de un circulo")  
    print("2. Area de un cuadrado")
    print("3. Par o impar")
    print("4. Calcule la hipotenusa de un triangulo rectangulo")
    print("5. Interes simple de un monto: ")
    print("6. Comparacion de 3 numeros: ")
    print("7. Vereficacion de Conctraseña: ")
    print("8. Salir: ")


while True:   #Realizamos un bucle buleano while para que el munu se pepita hasta que sea cerrado por el usuario con un false
    menu ()
    try: 
        option = int(input("Ingrese una opcion: "))
        
    except ValueError:
        print("Ingrese un numero valido")
        continue
    match option: 
        case 1:
            area_circulo()
        case 2:
            area_cuadrado()

        case 3: 
            par_impar()
                
        case 4:
            hipotenusa()

        case 5:
            interes()
            
        case 6:
            comparacion_numeros()
            
        case 7:
            contraseña()

        case 8:
            print("Fin del programa")
            break
            



