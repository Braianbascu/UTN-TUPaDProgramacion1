# Actividad Nº12

# Variables a usar


numeros = []

# Validacion de numeros
for i in range(8):
    while True:
        numero = input("Ingrese un numero entero: ")

        if numero == "":
            print("Debe ingresar un valor")
        elif not numero.isdigit():
            print("Solo se admiten valores numericos")
        else:
            numeros.append(int(numero))
            break

# Ordenamiento de listas
numeros_ordenados = sorted(numeros)
numeros_inversos = sorted(numeros_ordenados, reverse=True)

print("Su Lista de numeros")
print("")

# Muestra por interaccion (consigna)
print("De menor a mayor")
for numero in numeros_ordenados:
    print(f"Numero: {numero}")

print("")

print("De mayor a menor")
for numero in numeros_inversos:
    print(f"Numero: {numero}")
