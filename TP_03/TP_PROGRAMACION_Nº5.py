# Actividad Nº5

# Ingreso de segundos

segundos = int(input("Por favor ingrese los segundos a convertir en horas: "))


# Definicion de funcion
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas


resultado_segundos_a_horas = segundos_a_horas(segundos)

print(f"Los segundos ingresados equivalen a : {resultado_segundos_a_horas:.2f} horas")
