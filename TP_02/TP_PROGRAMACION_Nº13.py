# Actividades Nº13
# En esta actividad final se utilizaron metodos, no solo logica para resolver algunos items

# Variables a usar
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

mayor_puntaje = 0
menor_puntaje = 0

# Busqueda con metodso
mayor_puntaje = max(puntajes)
menor_puntaje = min(puntajes)

# Ordenamiento de lista
ranking = sorted(puntajes, reverse=True)

posicion = 1

# Muestra por interaccion (consigna)
for puntos in ranking:
    print(f"{posicion}º puesto: {puntos} puntos")
    posicion += 1

# Buscar el numero
posicion_numero = ranking.index(990)

print(f"mayor puntaje: {mayor_puntaje}")
print(f"menor puntaje: {menor_puntaje}")
print(f"La posicion del puntaje 990, es: {posicion_numero}")
