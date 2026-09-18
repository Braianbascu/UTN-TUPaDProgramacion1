# Actividad Nº9

# Variables a solicitar:

celsius = float(input("Ingrese su temperatura en Celsius: "))


# Definicion de funcion


def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


resultado = celsius_a_fahrenheit(celsius)

print(f"Su temperatura convertida a fahrenheit es de: {resultado:.2f}")
