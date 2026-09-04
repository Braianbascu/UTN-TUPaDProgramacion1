# Actividad Nº8

# Variables a usar

notas = [
    [5, 7, 8],
    [9, 5, 7],
    [3, 8, 9],
    [10, 5, 6],
    [4, 8, 7],
]

suma_materia_1 = 0
suma_materia_2 = 0
suma_materia_3 = 0

promedios = []

print("Gestor de notas de alumnos")
# Calculo individual por estudiantes
for i in range(5):
    suma = 0

    for n in range(3):
        suma += notas[i][n]

    promedio = suma / 3
    print(f"El promedio del estudainte Nº{i+1} es de: {promedio:.2f}")

# Calculo por materia
for i in range(5):
    suma_materia_1 += notas[i][0]
    suma_materia_2 += notas[i][1]
    suma_materia_3 += notas[i][2]

promedios.append(suma_materia_1 / 5)
promedios.append(suma_materia_2 / 5)
promedios.append(suma_materia_3 / 5)

# Impresion de promedios por ciclo (consigna)
for i in range(3):
    print(f"El promedio de la materia Nº{i+1} es: {promedios[i]:.2f}")
