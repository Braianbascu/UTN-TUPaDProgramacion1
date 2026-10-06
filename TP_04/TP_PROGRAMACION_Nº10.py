# Actividad Nº10

# Actividad Nº10

# Diccionario base
diccionario_base = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "España": "Madrid",
    "Francia": "Paris",
    "Japon": "Tokio",
    "Rusia": "Moscu",
}

# Diccionario nuevo
diccionario_nuevo = {}

# Invertir con bucle
for pais, capital in diccionario_base.items():
    diccionario_nuevo[capital] = pais

# Impresiond de resultados
print("--- Diccionario original ---")
print(diccionario_base)

print("")
print("--- Diccionario invertido ---")
print(diccionario_nuevo)
