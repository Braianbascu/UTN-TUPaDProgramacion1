# TRABAJO PRACTICO DE PROGRAMACION Nº1 - BASCUÑAN BRAIAN

# EJERCICIO Nº1

# Variable utiilizada

notas = []

for i in range(10):

    while True:
        nota = input("Ingrese la nota del estudiante: ")
        if nota == "":
            print("Debe ingresar un valor para continuar")
        elif not nota.isdigit():
            print("Debe ingresar un valor numerico")
        elif float(nota) < 0 or float(nota) > 10:
            print("Debe ingresar un valor entre el 0 al 10")
        else:
            nota = float(nota)
            notas.append(nota)
            break

# Calculo promedio
promedio = sum(notas) / len(notas)
nota_mayor = max(notas)
nota_menor = min(notas)

print("")
print("")
print("----LISTA Y RESUMEN DE NOTA----")
for i in range(len(notas)):
    print(f"Nota alumno: {i + 1} : {notas[i]}")

print("")
print("")
print(f"La nota promedio es: {promedio} ")
print(f"La nota mayor es: {nota_mayor}")
print(f"La nota menor es: {nota_menor}")
