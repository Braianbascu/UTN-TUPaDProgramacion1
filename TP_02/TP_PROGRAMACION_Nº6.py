# Actividad Nº6

# Variables a usar
numeros = [1, 2, 3, 4, 5, 6, 7]

ultimo = numeros[-1]

for i in range(len(numeros) - 1, 0, -1):
    numeros[i] = numeros[i - 1]

numeros[0] = ultimo

for numero in numeros:
    print(numero)
