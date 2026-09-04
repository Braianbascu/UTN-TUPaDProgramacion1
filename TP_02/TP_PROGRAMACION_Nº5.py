# Actividad Nº5

# Variable usada
estudiantes = [
    "Juan",
    "Braian",
    "Bruno",
    "Federico",
    "Leila",
    "Julieta",
    "Daiana",
    "Marcela",
]

print("---SISTEMA DE ALUMNOS---")
print(f"{estudiantes}")
print("")
print("")

# Menu de seleccion
while True:
    print("Seleccione la accion a realizar")
    print("")
    print("1: Agregar alumno")
    print("2: Eliminar alumno")

    opcion = input("Ingrese su eleccion: ")
    print("")
    # Validaciones opciones
    if opcion == "":
        print("Debe ingresar un valor")
        print("")
    elif not opcion.isdigit():
        print("Debe ingresar un valor numerico")
        print("")
    else:
        opcion = int(opcion)
        if opcion < 1 or opcion > 2:
            print("Error opcion fuera de rango")
            print("")
        else:
            break
# Validaciones seleccion
if opcion == 1:
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre == "":
            print("Debe ingresar un nombre")
        elif not nombre.isalpha():
            print("La carga solo admite letras")
        else:
            estudiantes.append(nombre)
            print("Estudiante agregado")
            break
else:
    while True:
        nombre = input("Ingrese el nombre del estudiante a eliminar: ")

        if nombre == "":
            print("Debe ingresar un nombre")
        elif not nombre.isalpha():
            print("La carga solo admite letras")
        elif nombre not in estudiantes:
            print("El estudiante no se encuentra en la lista")
        else:
            estudiantes.remove(nombre)
            print("Estudiante eliminado")
            break

print("")
print("---LISTA FINAL DE ESTUDIANTES")
print(f"{estudiantes}")
