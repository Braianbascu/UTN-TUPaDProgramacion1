# Actividad Nº3

# Variables a usar
precios_frutas = {
    "Banana": 1330,
    "Ananá": 2500,
    "Melón": 2800,
    "Uva": 1450,
    "Naranja": 1200,
    "Manzana": 1700,
    "Pera": 2300,
}

print(f"La lista completa con par clave valor: {precios_frutas}")

# Extraccion de claves y conversion a lista
lista_frutas = list(precios_frutas.keys())

print(f"La lista solo con las claves: {lista_frutas}")
