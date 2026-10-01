# Actividada Nº6

# Varibales a usar

alumnos = {}

# Ingreso de datos

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")

    notas = []

    for i in range(3):
        nota = float(input("Ingrese su nota: "))
        notas.append(nota)

    notas = tuple(notas)
    alumnos[nombre] = notas

# Ciclo impresion en consola
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2F}")
