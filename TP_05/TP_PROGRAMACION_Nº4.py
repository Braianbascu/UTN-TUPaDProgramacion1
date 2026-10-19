# Actividad Nº4

# Codigos con Try-Except (aclarando su tipo)

# 1

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")

except TypeError:
    print("Ocurrio un error al ingresar un tipo de dato no valido para la operacion")

except Exception as e:
    print(f"Ocurrio un error al intentar realizar la division: {e}")

# 2

try:
    numbers = [
        1,
        2,
        3,
    ]
    print(numbers[5])

except IndexError:
    print("No se puede acceder al elemento ya que este no existe dentro de la lista")

except Exception as e:
    print(f"Ocurrio un error al intentar acceder: {e}")
