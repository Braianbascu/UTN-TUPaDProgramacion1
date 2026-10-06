# Actividad Nº7

# Lista de asistencias
asistencias = [
    "Juan",
    "Pedro",
    "Ana",
    "Maria",
    "Juan",
    "Ana",
    "Dario",
    "Maria",
    "Maria",
    "Pedro",
]

contador_asistencias = {}


# Set para eliminar nombres repetidos
asistencias_filtradas = set(asistencias)


# Contador asistencias
for asistencia in asistencias:
    if asistencia in contador_asistencias:
        contador_asistencias[asistencia] += 1
    else:
        contador_asistencias[asistencia] = 1


# Impresion por consola
print("Lista original de asistencias:")
print(asistencias)
print("\nEmpleados que asistieron al menos una vez:")
print(asistencias_filtradas)
print("\nCantidad de asistencias por empleado:")
print(contador_asistencias)
