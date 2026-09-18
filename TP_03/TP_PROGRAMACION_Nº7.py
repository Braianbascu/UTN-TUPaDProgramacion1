# Actividad

# Variables a solicitar:

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))


# Definicion de funcion:


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    return (suma, resta, multiplicacion, division)


resultados = operaciones_basicas(num1, num2)

print(
    f"Las operaciones de tus dos numeros son: suma = {resultados[0]}, resta = {resultados[1]}, multiplicacion = {resultados[2]} y division = {resultados[3]:.2f} "
)
