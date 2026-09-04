# Actividad Nº7

# Variable a usar
temperaturas = [
    [5, 16],
    [8, 12],
    [9, 22],
    [7, 11],
    [7, 21],
    [12, 18],
    [4, 21],
]

suma_minimas = 0
suma_maximas = 0
mayor_aptitud = 0
dia_mayor_aptitud = 0


# Acumulacion de temperaturas y promedio
for i in range(7):
    suma_minimas += temperaturas[i][0]
    suma_maximas += temperaturas[i][1]

promedio_minima = suma_minimas / 7
promedio_maxima = suma_maximas / 7

# Calculo del dia
for i in range(7):
    calculo = temperaturas[i][1] - temperaturas[i][0]

    if calculo > mayor_aptitud:
        mayor_aptitud = calculo
        dia_mayor_aptitud = i

print("---RESUMEN SEMANAL DE TEMPERATURAS---")
print("")
print(f"Promedio semanal de minima: {promedio_minima:.2f}")
print(f"Promedio semanal de maximas: {promedio_maxima:.2f}")
print(
    f"El dia que mayor aptitud termica se registro fue el dia {dia_mayor_aptitud} de la semana"
)
