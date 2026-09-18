# Actividad Nº10

# Variables a solicitar:

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

# Definicion de funcion


def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


resultado = calcular_promedio(num1, num2, num3)

print(f"El promedio de tus numero es de: {resultado}")
