

#Ten encuenta los 3 procesos escenciales
#--Entrada
#--Proceso
#--Salida

##--Serie de Fibonachi Ademas que imprima la suma 


def leer_entero(prompt: str) -> int:
    """Pide un entero al usuario y reintenta hasta que la entrada sea válida."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

print("Cantidad de números pares, impares, positivos, negativos, neutros")
print("Ingresa 5 números:")

# Inicializamos variables
positivos = 0
negativos = 0
neutros = 0
pares = 0
impares = 0

for i in range(5):
    number = leer_entero(f"Número {i+1}: ")

    if number > 0:
        positivos += 1
    elif number < 0:
        negativos += 1
    else:
        neutros += 1

    # par / impar
    if number % 2 == 0:
        pares += 1
    else:
        impares += 1

print(
    f"Hay {positivos} positivos, {negativos} negativos, "
    f"{pares} pares, {impares} impares y {neutros} neutros"
)




