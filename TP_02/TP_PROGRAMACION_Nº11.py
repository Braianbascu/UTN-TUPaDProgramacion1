# Actividad Nº11

# Variables a usar

nombres = [
    "PEDRO",
    "BRAIAN",
    "RAMON",
    "JUAN",
    "MATIAS",
    "LEILA",
    "DAIANA",
    "JUANA",
    "MARTA",
    "MARIA",
]

print("Sistema de registros")
print("")

# Validar el nombre
while True:

    # Input convertido a mayusucla para evitar conflicto en la buisqueda
    nombre = input("Ingrese el nombre del estudiante a buscar: ").upper()

    if nombre == "":
        print("Debe ingresar una opcion")
    elif not nombre.isalpha():
        print("El campo solo puede tener letras")
    else:
        break

if nombre in nombres:
    posicion = nombres.index(nombre)
    print(f"El nombre {nombre} se encuentra en la lista.")
    print(f"Su posición es: {posicion + 1}")
else:
    print(f"El nombre {nombre} no se encuentra en la lista.")
