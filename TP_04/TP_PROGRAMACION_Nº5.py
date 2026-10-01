# Actividada Nº5

# Variable a usar
cantidad_palabras = {}

# Ingreso de frase a analizar
frase = input("Ingrese una frase: ")


palabras = frase.split()
palabras_unicas = set(palabras)

# Contador de palabras
for palabra in palabras:
    if palabra in cantidad_palabras:
        cantidad_palabras[palabra] += 1
    else:
        cantidad_palabras[palabra] = 1

# Impresion por consola
print(f"Palabras únicas: {palabras_unicas}")
print(f"tu frase tiene el siguiente recuento: {cantidad_palabras}")
