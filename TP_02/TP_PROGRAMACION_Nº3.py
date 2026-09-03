# Actividada Nº3

# importacionees
import random

# variables usadas
numeros = []
par = []
impar = []

# Generar la lista inicial
for i in range(15):
    numeros.append(random.randint(1, 100))

# Asignar a la lista correspondiente
for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("---Resumen Numeros---")
print("")
print(f"La lista de pares tiene: {len(par)}")
print("")
print(f"La lista de impares tiene: {len(impar)}")
print("")
print("---Listas---")
print(f"Lista par: {par}")
print(f"Lista impar: {impar}")
