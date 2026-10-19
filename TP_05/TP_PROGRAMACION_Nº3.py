# Actividad Nº3

# Codigos con Try-Except

# 1

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")
except:
    print("Ocurrio un error al intentar realizar la division")

# 2

try:
    numbers = [
        1,
        2,
        3,
    ]
    print(numbers[5])
except:
    print("Ocurrio un error al intentar acceder al elemento")
