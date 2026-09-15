# Actividad Nº4

# Importaciones
import math

# Solicitar radio
radio = float(input("Ingrese el radio de su circulo: "))


# Definicion de funciones:
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro


def calcular_area_circulo(radio):
    area = math.pi * radio * radio
    return area


# Llamado a las funciones
resultado_perimetro = calcular_perimetro_circulo(radio)
resultado_area = calcular_area_circulo(radio)


# Visualizacion por consola
print(f"Su perimetro es de: {resultado_perimetro}")
print(f"Su area es de: {resultado_area}")
